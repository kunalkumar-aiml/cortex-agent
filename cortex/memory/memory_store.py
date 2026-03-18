def search(self, task):

    data = self.load()

    if not data:
        return None

    query_embedding = self.model.encode(task)

    similarities = []

    valid_items = []

    for item in data:

        # skip old memory entries without embedding
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
