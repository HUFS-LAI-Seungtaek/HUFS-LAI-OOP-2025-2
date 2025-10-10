def label_distribution(labels: list[str]) -> dict[str, int]:
    distribution = {}
    for label in labels:
        distribution[label] = distribution.get(label, 0) + 1
    return distribution