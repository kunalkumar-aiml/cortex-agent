class AgentExecutor:

    def __init__(self, tools):

        self.tools = tools


    def run(self, task):

        print("Searching using tools...")

        search_results = self.tools["browser"].search_google(task)

        laptops = []

        for r in search_results:

            laptops.append({
                "name": r
            })

        return laptops
