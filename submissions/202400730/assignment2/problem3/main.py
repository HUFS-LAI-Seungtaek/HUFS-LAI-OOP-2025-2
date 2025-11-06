# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""
from collections import Counter

def count_tokens(tokens: list[str]) -> dict[str, int]:
    """
    Calculates the frequency of each token in a list.
    """
    # TODO: 구현하세요
    # 힌트: 2) 각 토큰을 순회하면서 카운트: d[token] = d.get(token, 0) + 1
    
    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1
    return d
    
    

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    """
    Returns the top k tokens and their frequencies, sorted by:
    1. Frequency (Descending)
    2. Token (Ascending, for tie-breaking)
    """
    # TODO: 구현하세요
    
    # 1) k <= 0인 경우 빈 리스트 반환
    if k <= 0:
        return []
        
    # 2) 딕셔너리를 (토큰, 빈도) 튜플 리스트로 변환
    items = list(freqs.items())
    
    # 3) 정렬 기준: (-frequency, token)
    # frequency에 마이너스를 붙여서 내림차순 정렬 효과를 내고, 
    # token으로 묶어 오름차순(기본값)으로 묶어서 동점 처리
    
    # lambda x: x[1]은 빈도(frequency), x[0]은 토큰(token)
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    # 4) 슬라이싱으로 상위 k개만: [:k]
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    """
    Merges multiple frequency dictionaries into a single dictionary, summing counts.
    """
    # TODO: 구현하세요 (선택사항)
    
    result = {}
    # 2) 각 딕셔너리를 순회: for freq_dict in maps
    for freq_dict in maps:
        # 3) 각 키-값을 누적
        for token, count in freq_dict.items():
            result[token] = result.get(token, 0) + count
            
    return result

    


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        # count_tokens 테스트
        tokens = ["hello","world","hello","ai", "world", "zoo"]
        f = count_tokens(tokens)            # {'hello': 2, 'world': 2, 'ai': 1, 'zoo': 1}
        print(f"Count: {f}")
        
        # top_k 테스트
        # k=2: ('hello', 2), ('world', 2) 동점 -> 토큰 오름차순(ai < hello)에 따라 ('hello', 2), ('world', 2) 중 선택
        # 실제로는 알파벳 순: ai < hello < world < zoo
        # 1. 빈도 2: hello, world
        # 2. 빈도 1: ai, zoo
        
        # k=3: 빈도 2인 토큰 (hello, world)와 빈도 1인 토큰 중 가장 빠른 토큰 (ai)
        top3 = top_k(f, 3) 
        print(f"Top 3: {top3}")             # [('hello', 2), ('world', 2), ('ai', 1)] (토큰 오름차순으로 동점 처리: 'hello' < 'world')
        
        top2 = top_k(f, 2)
        print(f"Top 2: {top2}")             # [('hello', 2), ('world', 2)]
        
        top10 = top_k(f, 10)
        print(f"Top 10: {top10}")           # 전체 리스트 반환
        
        empty_k = top_k(f, 0)
        print(f"Top 0: {empty_k}")          # []
        
        # merge_freqs 테스트
        g = merge_freqs([{"x": 1}, {"x": 2, "y": 3}, {"z": 1, "y": 1}])
        print(f"Merged: {g}")               # {'x': 3, 'y': 4, 'z': 1}
        
        print("\nDemo completed.")
        
    run_demo()
    # pass