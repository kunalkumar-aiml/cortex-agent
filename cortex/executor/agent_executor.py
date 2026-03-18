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

        print("\nCreating execution plan...\n")

        plan = self.planner.create_plan(task)

        print("PLAN:\n")
        print(plan)

        print("\nGenerating final recommendation...\n")

        prompt = f"""
You are a tech expert.

Task: {task}

Give the TOP 5 BEST laptops under ₹80,000 for gaming.

Rules:
- Only return laptop model names
- Include CPU and GPU
- Do NOT explain steps
- Format as numbered list
Example:
1. Laptop Model (CPU, GPU)
"""

        answer = self.planner.create_plan(prompt)

        results = [answer]

        self.memory.save(task, results)

        return results
