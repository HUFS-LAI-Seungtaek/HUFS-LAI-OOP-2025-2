

def label_distributuion(labels: list[str]) -> dict[str, int]:
    """
    입력 list를 순회하며 label별 빈도를 기록한 dictionary 반환
    """
    d={}
    for label in lables:
        d[label] = d.get(label,0) + 1
    
    return d