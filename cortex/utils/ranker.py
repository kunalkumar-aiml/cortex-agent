import re
from collections import Counter
from cortex.memory.feedback_store import FeedbackStore


class ProductRanker:

    def __init__(self):

        self.feedback = FeedbackStore()

    def extract_products(self, search_results):

        products = []

        for text in search_results:

            matches = re.findall(r"[A-Z][A-Za-z0-9\\- ]{4,}", text)

            for m in matches:

                clean = m.strip()

                if len(clean.split()) <= 6:
                    products.append(clean)

        return products

    def rank_products(self, products):

        counts = Counter(products)

        scores = self.feedback.get_scores()

        ranked = []

        for product, freq in counts.items():

            feedback_bonus = scores.get(product, 0)

            total_score = freq + feedback_bonus

            ranked.append((product, total_score))

        ranked.sort(key=lambda x: x[1], reverse=True)

        return [p[0] for p in ranked[:10]]
