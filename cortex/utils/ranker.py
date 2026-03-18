import re
from collections import Counter


class ProductRanker:

    def extract_products(self, search_results):

        products = []

        for text in search_results:

            matches = re.findall(r"[A-Z][A-Za-z0-9\\- ]{4,}", text)

            for m in matches:
                if len(m.split()) <= 6:
                    products.append(m.strip())

        return products

    def rank_products(self, products):

        counts = Counter(products)

        ranked = [item[0] for item in counts.most_common(10)]

        return ranked
