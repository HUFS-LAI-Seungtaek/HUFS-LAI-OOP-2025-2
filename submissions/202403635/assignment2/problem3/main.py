# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    # TODO: 구현하세요
    # 힌트:
    # 1) 빈 딕셔너리 생성: d = {}
    d = {}
    # 2) 각 토큰을 순회하면서 카운트: d[token] = d.get(token, 0) + 1
    for token in tokens:
        # .get(token, 0)은 딕셔너리에 token이 있으면 그 값을, 없으면 기본값 0을 반환합니다.
        # 이를 통해 토큰이 처음 등장할 때도 오류 없이 1을 더할 수 있습니다.
        d[token] = d.get(token, 0) + 1
    return d
    # 3) 또는 collections.Counter 사용 가능 (하지만 직접 구현도 간단함)

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    # TODO: 구현하세요
    # 힌트:
    # 1) k <= 0인 경우 빈 리스트 반환
    if k <= 0:
        return []
    # 2) sorted() 함수의 key 매개변수 활용
    # 3) 정렬 기준: (-frequency, token) -> 빈도 내림차순, 토큰 오름차순
    sorted_items = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))#gemini의 도움을 받음
    # 4) 슬라이싱으로 상위 k개만: [:k]
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    # TODO: 구현하세요 (선택사항)
    # 힌트:
    # 1) 결과 딕셔너리 생성: result = {}
    result = {}
    # 2) 각 딕셔너리를 순회: for freq_dict in maps
    for freq_dict in maps:
        for key, value in freq_dict.items():
            result[key] = result.get(key, 0) + value
        
    # 3) 각 키-값을 누적: result[key] = result.get(key, 0) + value
    return result


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)         # {'hello':2,'world':1,'ai':1}
        print(f)
        print(top_k(f, 2))               # [('hello',2),('ai',1)] or [('hello',2),('world',1)] (tie by token asc)
        g = merge_freqs([{"x":1},{"x":2,"y":3}])
        print(g)                         # {'x':3,'y':3}
    run_demo()
