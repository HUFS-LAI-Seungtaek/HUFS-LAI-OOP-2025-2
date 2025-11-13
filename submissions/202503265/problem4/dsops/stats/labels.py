def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    라벨 리스트를 받아 각 라벨의 빈도수를 계산합니다.
    """
    freqs = {}
    for label in labels:
        freqs[label] = freqs.get(label, 0) + 1
    return freqs