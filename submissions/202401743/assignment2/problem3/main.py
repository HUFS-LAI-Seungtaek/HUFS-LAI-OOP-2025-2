# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""
def count_tokens(tokens: list[str]) -> dict[str, int]:
    freqs = {}
    for token in tokens:
        freqs[token] = freqs.get(token,0) + 1
    return freqs
 # 9-10 Gemini 참고하였습니다.

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <=0:
        return []
    items =list(freqs.items())
    sorted_items = sorted(items,key = lambda item: (-item[1],item[0]))
    return sorted_items[:k]
    # 18 Gemini 참고하였습니다.

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for freq_dict in maps:
        for key,value in freq_dict.items():
            result[key] = result.get(key,0) + value
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
