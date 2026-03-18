import json
import os


class MemoryStore:

    def __init__(self, file_path="memory.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def save(self, task, result):

        with open(self.file_path, "r") as f:
            data = json.load(f)

        entry = {
            "task": task,
            "result": result
        }

        data.append(entry)

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def search(self, task):

        with open(self.file_path, "r") as f:
            data = json.load(f)

        task = task.lower()

        for item in data:
            if any(word in item["task"].lower() for word in task.split()):
                return item["result"]

        return None
