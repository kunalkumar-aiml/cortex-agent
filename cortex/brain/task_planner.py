from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class TaskPlanner:
    """
    AI powered task planner.
    Converts a user goal into a step-by-step plan.
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.3
        )

    def create_plan(self, task: str):

        prompt = f"""
You are an intelligent AI planning system.

Break the following goal into clear execution steps.

Goal:
{task}

Return a numbered list of steps.
"""

        response = self.llm.invoke(prompt)

        return response.content
