import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class MemoryStore:

    def __init__(self, file_path="memory.json"):

        self.file_path = file_path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def load(self):

        with open(self.file_path, "r") as f:
            return json.load(f)

    def save(self, task, result):

        data = self.load()

        embedding = self.model.encode(task).tolist()

        entry = {
            "task": task,
            "result": result,
            "embedding": embedding
        }

        data.append(entry)

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def search(self, task):

        data = self.load()

        if not data:
            return None

        query_embedding = self.model.encode(task)

        similarities = []
        valid_items = []

        for item in data:

            if "embedding" not in item:
                continue

            emb = np.array(item["embedding"]).reshape(1, -1)

            sim = cosine_similarity(
                [query_embedding], emb
            )[0][0]

            similarities.append(sim)
            valid_items.append(item)

        if not similarities:
            return None

        best_index = int(np.argmax(similarities))

        if similarities[best_index] > 0.7:
            return valid_items[best_index]["result"]

        return None
