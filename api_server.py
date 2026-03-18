from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from cortex.brain.task_planner import TaskPlanner
from cortex.executor.agent_executor import AgentExecutor
from cortex.tools.browser_tool import BrowserTool


app = FastAPI(title="Cortex Agent API")

# CORS fix so browser UI can talk to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

planner = TaskPlanner()

tools = {
    "browser": BrowserTool()
}

executor = AgentExecutor(planner, tools)


class Query(BaseModel):
    task: str


@app.post("/ask")
def ask_agent(query: Query):

    result = executor.run(query.task)

    return {
        "query": query.task,
        "result": result
    }
