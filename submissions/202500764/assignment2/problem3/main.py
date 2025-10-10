# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    freqs = {}
    for token in tokens:
        freqs[token] = freqs.get(token, 0) + 1
    return freqs

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]
   #tok_k구현하는 과정에서 지피티 사용해서 코드 받아서 사용했습니다.


def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    merged = {}
    for freq_dict in maps:
        for token, count in freq_dict.items():
            merged[token] = merged.get(token, 0) + count
    return merged
    #이 부분도 지피티 사용해서 코드 받아서 사용했습니다.
if __name__ == "__main__":
    def run_demo():
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)         # {'hello':2,'world':1,'ai':1}
        print("Token frequencies:", f)
        print("Top 2 tokens:", top_k(f, 2))   # [('hello',2),('ai',1)]
        g = merge_freqs([{"x":1},{"x":2,"y":3}])
        print("Merged freqs:", g)             # {'x':3,'y':3}

    run_demo()
