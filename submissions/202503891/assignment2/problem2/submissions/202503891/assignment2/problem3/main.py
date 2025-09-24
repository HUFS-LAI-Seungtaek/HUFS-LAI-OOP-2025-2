def count_tokens(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    # (빈도 내림차순, 동률일 땐 토큰 오름차순)
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]

def merge_freqs(maps: list[dict[str,int]]) -> dict[str,int]:
    merged = {}
    for freq_map in maps:
        for token, count in freq_map.items():
            merged[token] = merged.get(token, 0) + count
    return merged

if __name__ == "__main__":
    # 데모 코드 (실행 시 출력)
    tokens = ["a", "b", "a"]
    print("count_tokens:", count_tokens(tokens))
    freqs = {"a": 2, "b": 2, "c": 1}
    print("top_k(2):", top_k(freqs, 2))
    print("merge_freqs:", merge_freqs([{"a":1}, {"a":2, "b":1}]))
