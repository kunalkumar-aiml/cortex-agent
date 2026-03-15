from cortex.brain.task_planner import TaskPlanner


def main():

    planner = TaskPlanner()

    task = input("Enter your task: ")

    plan = planner.create_plan(task)

    print("\nGenerated Plan:\n")

    for step in plan:
        print("-", step)


if __name__ == "__main__":
    main()
