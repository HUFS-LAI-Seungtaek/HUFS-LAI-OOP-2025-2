"""
Label statistics utilities for dataset analysis.
"""


def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    레이블 리스트에서 각 레이블의 빈도를 계산합니다.
    
    Args:
        labels: 레이블 문자열 리스트
        
    Returns:
        각 레이블과 그 빈도를 담은 딕셔너리
        
    Examples:
        >>> label_distribution(["cat", "dog", "cat"])
        {'cat': 2, 'dog': 1}
    """
    # 빈도 카운터 초기화
    freq_counter = {}
    
    # 각 레이블의 빈도 계산
    for label in labels:
        freq_counter[label] = freq_counter.get(label, 0) + 1
    
    return freq_counter