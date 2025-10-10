from collections import Counter

def label_distribution(labels: list[str]) -> dict[str, int]:
    return dict(Counter(labels))
