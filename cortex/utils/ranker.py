import re

def rank_products(products):

    ranked = []

    for p in products:

        score = 0

        text = p.lower()

        if "rtx 4050" in text:
            score += 10

        if "rtx 3050" in text:
            score += 8

        if "ryzen 7" in text:
            score += 7

        if "i7" in text:
            score += 7

        if "ryzen 5" in text:
            score += 6

        if "i5" in text:
            score += 6

        ranked.append((p, score))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return [x[0] for x in ranked]
