from cortex.memory.memory_store import MemoryStore
from cortex.utils.ranker import ProductRanker
from cortex.memory.feedback_store import FeedbackStore


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()
        self.ranker = ProductRanker()
        self.feedback = FeedbackStore()

    def run(self, task):

        print("\nSearching using tools...\n")

        results = []

        if "browser" in self.tools:

            res = self.tools["browser"].search_google(task)

            products = self.ranker.extract_products(res)

            ranked = self.ranker.rank_products(products)

            results.extend(ranked)

        final_prompt = f"""
User Query: {task}

Detected Products:
{results}

Rules:

Return only recommendations.

Format:

Top 5 Best Options:

1. Product
2. Product
3. Product
4. Product
5. Product

If slightly increasing the budget gives better options:

Better options if budget increases slightly:

• Product
• Product
"""

        answer = self.planner.create_plan(final_prompt)

        print("\nRecommendation:\n")
        print(answer)

        # Feedback learning
        print("\nDid you like the recommendations? (y/n)")

        feedback = input().strip().lower()

        if feedback == "y":

            for product in results[:5]:
                self.feedback.save_feedback(product, 1)

        elif feedback == "n":

            for product in results[:5]:
                self.feedback.save_feedback(product, -1)

        return [answer]
