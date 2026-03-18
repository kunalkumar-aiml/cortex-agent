from cortex.memory.memory_store import MemoryStore


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()

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

            results.extend(res)

        print("\nGenerating AI recommendation...\n")

        final_prompt = f"""
User Query: {task}

Search Results:
{results}

Rules for answering:

1. Give direct recommendations.
2. If the user asks for TOP or BEST items, return a numbered list.
3. Keep the answer short and clean.
4. If the budget is mentioned (example: under 80k), recommend items within that budget.
5. After the main list, suggest 1-2 better options if the user can increase the budget slightly (₹2k-₹5k more).
6. Do not explain planning or steps.

Example format:

Top 5 Best Options:

1. Item name
2. Item name
3. Item name
4. Item name
5. Item name

If you can increase your budget slightly, these are even better:

• Item name
• Item name
"""

        answer = self.planner.create_plan(final_prompt)

        self.memory.save(task, answer)

        return [answer]
