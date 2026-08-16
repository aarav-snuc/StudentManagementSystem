def plot_scores(scores):
    for roll, score in scores.items():
        print(roll, "|", "*" * int(score / 10))
