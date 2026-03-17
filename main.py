from cortex.brain.task_planner import TaskPlanner
from cortex.tools.browser_tool import BrowserTool


def main():

    planner = TaskPlanner()
    browser = BrowserTool()

    task = input("Enter your task: ")

    print("\nGenerating AI Plan...\n")

    plan = planner.create_plan(task)

    print("AI Generated Plan:\n")
    print(plan)

    print("\nRunning browser search...\n")

    results = browser.search_google(task)

    print("Top Search Results:\n")

    for r in results:
        print("-", r)


if __name__ == "__main__":
    main()
