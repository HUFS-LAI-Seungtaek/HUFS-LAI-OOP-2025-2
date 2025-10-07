# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    frequencies = {}
    for token in tokens:
        frequencies[token] = frequencies.get(token, 0) + 1
    return frequencies

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    
    sorted_tokens = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    return sorted_tokens[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    merged = {}
    for freq_map in maps:
        for token, count in freq_map.items():
            merged[token] = merged.get(token, 0) + count
    return merged

if __name__ == "__main__":
    def run_demo():
        tokens = ["hello", "world", "hello", "ai"]
        f = count_tokens(tokens)
        print(f)
        print(top_k(f, 2))
        g = merge_freqs([{"x": 1}, {"x": 2, "y": 3}])
        print(g)
    
    run_demo()