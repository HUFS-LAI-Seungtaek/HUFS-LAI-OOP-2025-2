# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    # TODO: 구현하세요
    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1
    return d
    # 힌트:
    # 1) 빈 딕셔너리 생성: d = {}
    # 2) 각 토큰을 순회하면서 카운트: d[token] = d.get(token, 0) + 1
    # 3) 또는 collections.Counter 사용 가능 (하지만 직접 구현도 간단함)

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    # TODO: 구현하세요
    if k <= 0:
        return []
    sorted_items = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
    # 힌트:
    # 1) k <= 0인 경우 빈 리스트 반환
    # 2) sorted() 함수의 key 매개변수 활용
    # 3) 정렬 기준: (-frequency, token) -> 빈도 내림차순, 토큰 오름차순
    # 4) 슬라이싱으로 상위 k개만: [:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    # TODO: 구현하세요 (선택사항)
    result = {}
    for freq_dict in maps:
        for key, value in freq_dict.items():
            result[key] = result.get(key, 0) + value
    return result
    # 힌트:
    # 1) 결과 딕셔너리 생성: result = {}
    # 2) 각 딕셔너리를 순회: for freq_dict in maps
    # 3) 각 키-값을 누적: result[key] = result.get(key, 0) + value


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
    pass
"""
(도움받은 내용):
이 모듈의 함수들을 구현하며 생성형 AI(Gemini)의 도움을 받았습니다.
- count_tokens: 딕셔너리의 .get() 메서드를 활용한 빈도수 계산법을 학습했습니다.
- top_k: sorted() 함수의 key와 lambda를 이용한 정렬 방법을 구현하는 데 도움을 받았습니다.
"""