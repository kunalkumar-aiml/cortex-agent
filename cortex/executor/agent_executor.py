from langchain_ollama import ChatOllama


class AgentExecutor:

    def __init__(self, tools):

        self.tools = tools

        # Local LLM
        self.llm = ChatOllama(model="llama3")


    def run(self, task):

        print("\nChecking memory...\n")

        print("\nSearching using tools...\n")

        # Search using browser tool
        search_results = self.tools["browser"].search_google(task)

        # Prompt for LLM
        prompt = f"""
You are an expert technology analyst and hardware reviewer.

User Query:
{task}

You must recommend the BEST and LATEST products available right now.

Important Rules:
- Only include models from 2024, 2025 or 2026
- Ignore old laptops
- Prefer latest CPU generation (Intel 13th/14th gen or Ryzen 7000/8000)
- Prefer RTX GPU if available
- Recommend only real laptops available in the market

Search Results:
{search_results}

Your job:

Give TOP 5 BEST OPTIONS.

For each laptop provide:

1. Laptop Name
2. CPU
3. GPU
4. RAM
5. Storage
6. Display
7. Why it is best

Format example:

1. Laptop Name

CPU:
GPU:
RAM:
Storage:
Display:

Why it is best:

Do NOT include old models.
Always prioritize the newest hardware.
"""

        response = self.llm.invoke(prompt)

        return response.content
