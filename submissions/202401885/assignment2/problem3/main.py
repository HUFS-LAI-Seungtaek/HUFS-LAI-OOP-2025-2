"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

from typing import List, Dict, Tuple

def count_tokens(tokens: List[str]) -> Dict[str, int]:
    """
    토큰 리스트에서 빈도 사전을 만듭니다.
    빈 입력이어도 {} 반환.
    """
    freq: Dict[str, int] = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq

def top_k(freqs: Dict[str, int], k: int) -> List[Tuple[str, int]]:
    """
    빈도 내림차순, 동률은 토큰 문자열 오름차순으로 정렬한 뒤 상위 k개를 반환합니다.
    k <= 0이면 [] 반환.
    """
    if k <= 0:
        return []
    return sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))[:k]

def merge_freqs(maps: List[Dict[str, int]]) -> Dict[str, int]:
    """
    (선택) 여러 빈도 맵을 합칩니다.
    """
    out: Dict[str, int] = {}
    for m in maps:
        for key, val in m.items():
            out[key] = out.get(key, 0) + int(val)
    return out


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)          # {'hello':2,'world':1,'ai':1}
        print(f)
        print(top_k(f, 2))                # [('hello',2),('ai',1)]  (동률은 토큰 오름차순이므로 'ai'가 'world'보다 먼저)
        g = merge_freqs([{"x":1},{"x":2,"y":3}])
        print(g)                          # {'x':3,'y':3}

    run_demo()
