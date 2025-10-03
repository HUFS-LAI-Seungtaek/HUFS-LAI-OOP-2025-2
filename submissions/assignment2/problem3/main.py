# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    # 힌트:
    # 1) 빈 딕셔너리 생성: d = {}
    # 2) 각 토큰을 순회하면서 카운트: d[token] = d.get(token, 0) + 1
    # 3) 또는 collections.Counter 사용 가능 (하지만 직접 구현도 간단함)
    freqs = {}
    for token in tokens:
        freqs[token] = freqs.get(token, 0) + 1
    return freqs

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    # 힌트:
    # 1) k <= 0인 경우 빈 리스트 반환
    # 2) sorted() 함수의 key 매개변수 활용
    # 3) 정렬 기준: (-frequency, token) -> 빈도 내림차순, 토큰 오름차순
    # 4) 슬라이싱으로 상위 k개만: [:k]
    if k <= 0:
        return []
    
    sorted_items = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    # 1) 결과 딕셔너리 생성: result = {}
    # 2) 각 딕셔너리를 순회: for freq_dict in maps
    # 3) 각 키-값을 누적: result[key] = result.get(key, 0) + value
    merged = {}
    for freq_map in maps:
        for token, count in freq_map.items():
            merged[token] = merged.get(token, 0) + count
    return merged


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        print("--- Demo Start ---")
        tokens = ["hello","world","hello","ai", "world", "hello"]
        print(f"Tokens: {tokens}")

        f = count_tokens(tokens)
        print(f"count_tokens -> {f}")
        
        top2 = top_k({"hello":2, "world":1, "ai":1}, 2)
        print(f"top_k with tie -> {top2}")
        
        g = merge_freqs([{"x":1, "y":10}, {"x":2, "y":3, "z":100}])
        print(f"merge_freqs -> {g}")
        print("--- Demo End ---")

    run_demo()