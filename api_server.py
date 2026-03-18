from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from cortex.tools.browser_tool import BrowserTool
from cortex.executor.agent_executor import AgentExecutor

app = FastAPI()

# allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tools = {
    "browser": BrowserTool()
}

executor = AgentExecutor(tools)


class Query(BaseModel):
    task: str


@app.get("/")
def home():
    return {"message": "Cortex AI Agent Running"}


@app.post("/ask")
async def ask(q: Query):

    result = executor.run(q.task)

    return {"result": result}
