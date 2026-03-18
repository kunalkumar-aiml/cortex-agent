from cortex.memory.memory_store import MemoryStore
from cortex.utils.ranker import ProductRanker


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()
        self.ranker = ProductRanker()

    def run(self, task):

        print("\nChecking memory...\n")

        memory_result = self.memory.search(task)

        if memory_result:
            print("Memory match found\n")
            return memory_result

        print("\nSearching using tools...\n")

        results = []

        if "browser" in self.tools:

            res = self.tools["browser"].search_google(task)

            products = self.ranker.extract_products(res)

            ranked = self.ranker.rank_products(products)

            results.extend(ranked)

        print("\nGenerating AI recommendation...\n")

        final_prompt = f"""
User Query: {task}

Detected Products:
{results}

Rules:
- Return only useful recommendations
- If user asks for TOP items, return a numbered list
- Keep the answer short
- Recommend products within the user's budget
- If slightly increasing the budget gives better products, suggest them

Example format:

Top 5 Best Options:

1. Product name
2. Product name
3. Product name
4. Product name
5. Product name

If you can increase the budget slightly, these are better:

• Product name
• Product name
"""

        answer = self.planner.create_plan(final_prompt)

        self.memory.save(task, answer)

        return [answer]
