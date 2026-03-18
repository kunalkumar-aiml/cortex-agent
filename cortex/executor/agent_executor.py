from cortex.memory.memory_store import MemoryStore


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()

    def run(self, task):

        print("\nChecking memory...\n")

        past = self.memory.load()

        for item in past:
            if task.lower() in item["task"].lower():
                print("Found similar task in memory\n")
                return item["result"]

        print("\nCreating execution plan...\n")

        plan = self.planner.create_plan(task)

        print("PLAN:\n")
        print(plan)

        print("\nExecuting tools...\n")

        results = []

        if "search" in task.lower() or "find" in task.lower():

            if "browser" in self.tools:

                res = self.tools["browser"].search_google(task)

                results.extend(res)

        self.memory.save(task, results)

        return results
