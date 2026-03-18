import json
import os
from collections import defaultdict


class FeedbackStore:

    def __init__(self, file_path="feedback.json"):

        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def load(self):

        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_feedback(self, product, score):

        data = self.load()

        if product not in data:
            data[product] = 0

        data[product] += score

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def get_scores(self):

        return self.load()
