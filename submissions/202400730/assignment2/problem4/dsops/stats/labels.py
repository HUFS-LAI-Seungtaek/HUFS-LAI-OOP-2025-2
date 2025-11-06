from collections import Counter

def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    리스트에 있는 각 레이블의 분포(빈도)를 계산합니다.

    Args:
        labels (list[str]): 레이블 문자열이 담긴 리스트.

    Returns:
        dict[str, int]: 각 레이블을 키로, 빈도를 값으로 갖는 딕셔너리.
    """
    
    return dict(Counter(labels))
