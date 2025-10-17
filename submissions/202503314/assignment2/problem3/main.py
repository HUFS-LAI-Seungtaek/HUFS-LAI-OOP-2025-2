def count_tokens(tokens: list[str]) -> dict[str, int]:
    d = {}
    for t in tokens:
        d[t] = d.get(t, 0) + 1
    return d

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for m in maps:
        for k, v in m.items():
            result[k] = result.get(k, 0) + v
    return result

if __name__ == "__main__":
    def run_demo():
        tokens = ["hello", "world", "hello", "ai"]
        f = count_tokens(tokens)
        print(f)
        print(top_k(f, 2))
        g = merge_freqs([{"x": 1}, {"x": 2, "y": 3}])
        print(g)
    run_demo()