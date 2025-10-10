def label_distribution(labels: list[str]) -> dict[str, int]:
    freq = {}
    for label in labels:
        freq[label] = freq.get(label, 0) + 1
    return freq
