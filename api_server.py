from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cortex.brain.task_planner import TaskPlanner
from cortex.tools.browser_tool import BrowserTool
from cortex.executor.agent_executor import AgentExecutor

from langchain_community.chat_models import ChatOllama


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Local LLM
llm = ChatOllama(model="llama3")

# Components
planner = TaskPlanner()

tools = {
    "browser": BrowserTool()
}

executor = AgentExecutor(planner, tools, llm)


@app.post("/ask")
async def ask(data: dict):

    task = data.get("task")

    result = executor.run(task)

    return {"result": result}
