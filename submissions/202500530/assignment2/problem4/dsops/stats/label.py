def label_distribution(labels: list[str]) -> dict[str, int]:
    d = {}
    for label in labels:
        d[label] = d.get(label, 0) + 1
    return d