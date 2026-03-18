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

        iteration = 0
        max_iterations = 3

        results = []

        while iteration < max_iterations:

            print(f"\nAgent Iteration {iteration+1}\n")

            print("Creating execution plan...\n")

            plan = self.planner.create_plan(task)

            print("PLAN:\n")
            print(plan)

            print("\nExecuting tools...\n")

            if "search" in task.lower() or "find" in task.lower():

                if "browser" in self.tools:

                    res = self.tools["browser"].search_google(task)

                    results.extend(res)

            if results:
                break

            iteration += 1

        print("\nGenerating final recommendation...\n")

        final_prompt = f"""
User task: {task}

Tool results:
{results}

Provide the final answer and recommendations clearly.
"""

        answer = self.planner.create_plan(final_prompt)

        self.memory.save(task, results)

        return [answer]
