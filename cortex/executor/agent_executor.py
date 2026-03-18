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

        print("\nGenerating answer using AI...\n")

        answer = self.planner.create_plan(
            f"Give top 5 best options with model names for: {task}"
        )

        results = [answer]

        self.memory.save(task, results)

        return results
