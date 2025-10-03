from collections import Counter

def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    라벨 리스트의 빈도 사전을 반환한다.
    """
    return dict(Counter(labels))
