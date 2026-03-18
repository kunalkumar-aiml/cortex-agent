class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools

    def run(self, task):

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

        return results
