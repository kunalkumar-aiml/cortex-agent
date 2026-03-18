from cortex.memory.memory_store import MemoryStore
from cortex.utils.ranker import rank_products


class AgentExecutor:

    def __init__(self, planner, tools, llm):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()
        self.llm = llm

    def run(self, task):

        print("\nChecking memory...\n")

        memory_result = self.memory.search(task)

        if memory_result:

            print("Memory match found\n")

            return memory_result

        print("\nSearching using tools...\n")

        search_results = self.tools["browser"].search_google(task)

        ranked = rank_products(search_results)

        context = "\n".join(ranked[:10])

        prompt = f"""
User query: {task}

Search results:
{context}

Instructions:

Give the latest recommendations based on search results.

Rules:

- Prefer products released after 2023
- Include specifications
- Explain why it is best
- Return top 5 products

Format:

Product Name

CPU:
GPU:
RAM:
Why best:
"""

        answer = self.llm.invoke(prompt)

        result = answer.content

        self.memory.save(task, result)

        return result
