marks_records = {}


def add_marks(roll, subject, score):
    marks_records.setdefault(roll, {})[subject] = score
    print("Marks added for", roll, ":", subject, "=", score)


def average_marks(roll):
    scores = marks_records.get(roll, {})
    if not scores:
        return 0
    return sum(scores.values()) / len(scores)
