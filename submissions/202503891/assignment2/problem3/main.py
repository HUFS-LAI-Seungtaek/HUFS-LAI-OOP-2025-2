from typing import List, Dict, Tuple

def count_tokens(tokens: List[str]) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq

def top_k(freqs: Dict[str, int], k: int) -> List[Tuple[str, int]]:
    if k <= 0:
        return []
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]

def merge_freqs(maps: List[Dict[str,int]]) -> Dict[str,int]:
    merged: Dict[str,int] = {}
    for m in maps:
        for k, v in m.items():
            merged[k] = merged.get(k, 0) + v
    return merged

if __name__ == "__main__":
    tokens = ["a", "b", "a", "c", "b", "a"]
    print("Token counts:", count_tokens(tokens))
    print("Top 2:", top_k(count_tokens(tokens), 2))
    merged = merge_freqs([{"a":1}, {"a":2,"b":1}])
    print("Merged freqs:", merged)
