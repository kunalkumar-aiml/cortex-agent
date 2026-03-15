class TaskPlanner:
    """
    TaskPlanner converts user goals into structured steps.
    """

    def __init__(self):
        self.name = "Cortex Planner"

    def create_plan(self, task: str):
        """
        Generate a basic execution plan from a user task.
        """

        steps = [
            "Understand the task",
            "Search relevant information",
            "Open required websites",
            "Collect useful results",
            "Return the best result"
        ]

        return steps
