import ollama


class TaskPlanner:

    def __init__(self):
        self.model = "llama3"

    def create_plan(self, task):

        prompt = f"""
You are an AI planning system.

Break the following goal into clear steps.

Goal:
{task}

Return numbered steps.
"""

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]
