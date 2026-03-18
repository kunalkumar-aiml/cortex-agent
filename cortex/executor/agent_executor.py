from cortex.memory.memory_store import MemoryStore


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()

    def select_tool(self, task):

        task = task.lower()

        if "search" in task or "find" in task or "best" in task:
            return "browser"

        return None

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

        tool = self.select_tool(task)

        results = []

        if tool == "browser":

            print("\nUsing Browser Tool...\n")

            res = self.tools["browser"].search_google(task)

            results.extend(res)

        if not results:

            print("\nGenerating AI recommendation...\n")

            prompt = f"""
You are a technology expert.

Task: {task}

Provide the TOP 5 best laptop recommendations.

Rules:
- Only return laptop model names
- Include CPU and GPU
- Do NOT explain steps
- Format as numbered list

Example:
1. Laptop Model (CPU, GPU)
"""

            answer = self.planner.create_plan(prompt)

            results.append(answer)

        self.memory.save(task, results)

        return results
