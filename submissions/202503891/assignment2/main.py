def count_tokens(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_k(freqs, k):
    if k <= 0:
        return []
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]

def merge_freqs(maps):
    merged = {}
    for freq in maps:
        for token, count in freq.items():
            merged[token] = merged.get(token, 0) + count
    return merged

if __name__ == "__main__":
    sample = ["apple", "banana", "apple", "orange", "banana", "banana"]
    freq = count_tokens(sample)
    print("Frequency:", freq)
    print("Top 2:", top_k(freq, 2))
    merged = merge_freqs([freq, {"banana": 1, "grape": 2}])
    print("Merged:", merged)
