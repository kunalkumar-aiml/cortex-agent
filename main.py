from cortex.brain.task_planner import TaskPlanner


def main():

    planner = TaskPlanner()

    task = input("Enter your task: ")

    plan = planner.create_plan(task)

    print("\nAI Generated Plan:\n")
    print(plan)


if __name__ == "__main__":
    main()
