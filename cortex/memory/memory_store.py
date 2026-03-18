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

        data.append({
            "task": task,
            "result": result
        })

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):

        with open(self.file_path, "r") as f:
            return json.load(f)
