from collections import Counter

def label_distribution(labels: list[str]) -> dict[str, int]:
    return dict(Counter(labels))

'''
리스트의 빈도 구하는 방법: https://wikidocs.net/84105
return Counter(labels) 상태로 출력하면 Counter({...,...}) 형태로 출력돼서
앞에 dict()를 넣어봤는데 깔끔하게 딕셔너리만 출력됐다!
'''