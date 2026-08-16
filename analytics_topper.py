def class_topper(scores):
    if not scores:
        return None
    return max(scores, key=scores.get)

