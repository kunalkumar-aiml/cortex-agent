import json
import os


class MemoryStore:

    def __init__(self):

        self.file = "memory.json"

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:

                json.dump([], f)

    def load(self):

        with open(self.file) as f:

            return json.load(f)

    def save(self, task, result):

        data = self.load()

        data.append({

            "task": task,
            "result": result

        })

        with open(self.file, "w") as f:

            json.dump(data, f)

    def search(self, task):

        data = self.load()

        for item in data:

            if task.lower() in item["task"].lower():

                return item["result"]

        return None
