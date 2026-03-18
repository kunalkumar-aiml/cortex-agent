from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from cortex.tools.browser_tool import BrowserTool
from cortex.executor.agent_executor import AgentExecutor

app = FastAPI()

# CORS (frontend ko allow karne ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tools
tools = {
    "browser": BrowserTool()
}

# Agent Executor
executor = AgentExecutor(tools)


# Request Model
class Query(BaseModel):
    task: str


@app.get("/")
def home():
    return {"message": "Cortex Agent API Running"}


@app.post("/ask")
async def ask(query: Query):

    task = query.task

    result = executor.run(task)

    return {
        "result": result
    }
