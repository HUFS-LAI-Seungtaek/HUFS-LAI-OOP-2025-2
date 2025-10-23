# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

from typing import Counter # 타입 힌트를 위해 Counter를 가져올 수 있음. (선택사항)
# 만약 collections.Counter를 사용한다면 import collections 필요

def count_tokens(tokens: list[str]) -> dict[str, int]:
    # TODO: 구현하세요
    
    # 힌트 2)를 사용하여 직접 구현
    d = {}
    for token in tokens:
        # 딕셔너리에 토큰이 없으면 0으로 시작, 있으면 현재 값에 1을 더함
        d[token] = d.get(token, 0) + 1
    return d

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    # TODO: 구현하세요
    
    # 1) k <= 0인 경우 빈 리스트 반환
    if k <= 0:
        return []

    # 딕셔너리 항목을 [('토큰', 빈도), ...] 리스트로 변환
    items = freqs.items()

    # 2), 3) 정렬 기준: (-frequency, token)
    # -frequency: 빈도를 내림차순으로 정렬하기 위해 마이너스(-)를 붙임 (파이썬 기본 정렬은 오름차순)
    # token: 빈도가 같을 때(동률일 때) 토큰 문자열을 오름차순으로 정렬 (타이브레이커)
    
    # 정렬 키 함수: lambda item: (-빈도, 토큰)
    sorted_items = sorted(items, key=lambda item: (-item[1], item[0]))
    
    # 4) 슬라이싱으로 상위 k개만 반환
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    # TODO: 구현하세요 (선택사항)
    
    # 힌트 2)와 3)을 사용하여 구현
    result = {}
    for freq_dict in maps:
        for key, value in freq_dict.items():
            # result에 이미 키가 있으면 값을 누적, 없으면 value로 초기화
            result[key] = result.get(key, 0) + value
            
    return result


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        # Example 1: count_tokens
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)        
        # 기대: {'hello': 2, 'world': 1, 'ai': 1}
        print(f"Counted Freqs: {f}")
        
        # Example 2: top_k (k=2)
        # 빈도 동률 테스트: 'world'와 'ai'는 빈도가 1로 같음. 사전순('ai' < 'world')으로 'ai'가 먼저 와야 함.
        top = top_k(f, 2)
        # 기대: [('hello', 2), ('ai', 1)]
        print(f"Top-2 (freq desc, token asc): {top}")
        
        # Example 3: merge_freqs
        g = merge_freqs([{"x":1, "y":2}, {"x":2, "z":3}])
        # 기대: {'x': 3, 'y': 2, 'z': 3}
        print(f"Merged Freqs: {g}")

        # Edge Case Test (k <= 0)
        print(f"Top-0: {top_k(f, 0)}") # 기대: []

    run_demo()