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

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    # TODO: 구현하세요
    if k <= 0:
        return []
    a = sorted(
        freqs.items(), key = lambda x:(-x[1], x[0])
    ) 
    return a[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    # TODO: 구현하세요 (선택사항)
    result = {}
    for b in maps:
        for ket,value in b.items():
            result[key]=result.get(key,0)+value
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
    pass