def rank_students(scores):
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
