# dsops/stats/labels.py

def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    주어진 레이블 리스트의 빈도 분포(단순 빈도 사전)를 계산합니다.
    """
    
    distribution = {}
    for label in labels:
        # get(key, default)를 이용해 안전하게 빈도 누적
        distribution[label] = distribution.get(label, 0) + 1
        
    return distribution