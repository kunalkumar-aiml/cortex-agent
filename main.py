from cortex.brain.task_planner import TaskPlanner
from cortex.tools.browser_tool import BrowserTool
from cortex.executor.agent_executor import AgentExecutor


def main():

    planner = TaskPlanner()

    browser = BrowserTool()

    tools = {
        "browser": browser
    }

    executor = AgentExecutor(planner, tools)

    task = input("Enter your task: ")

    results = executor.run(task)

    print("\nResults:\n")

    for r in results:
        print("-", r)


if __name__ == "__main__":
    main()
