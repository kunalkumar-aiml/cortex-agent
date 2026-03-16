from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class TaskPlanner:

    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.3)

    def create_plan(self, task):

        prompt = f"""
You are an AI planning system.

Break the following goal into clear steps.

Goal:
{task}

Return a numbered list.
"""

        response = self.llm.invoke(prompt)

        return response.content
