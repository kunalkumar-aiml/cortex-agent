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

        # disable memory for fresh answers
        memory_result = None

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

You are an expert recommendation AI.

STRICT RULES:

- Do NOT explain steps
- Do NOT show planning
- Do NOT write long paragraphs
- Only give recommendations

If the user asks for TOP or BEST items:

Return exactly this format:

Top 5 Best Options:

1. Product Name
2. Product Name
3. Product Name
4. Product Name
5. Product Name

After that, check if slightly increasing the budget would give much better options.

If yes, add:

Better options if you can increase the budget slightly (₹2000–₹5000):

• Product Name
• Product Name

Only return the recommendations.
"""

        answer = self.planner.create_plan(final_prompt)

        self.memory.save(task, answer)

        return [answer]
