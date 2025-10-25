from typing import List, Dict, Tuple
from collections import Counter

# --- ОСНОВНЫЕ ФУНКЦИИ ---

def count_tokens(tokens: List[str]) -> Dict[str, int]:
    return dict(Counter(tokens))

def top_k(freqs: Dict[str, int], k: int) -> List[Tuple[str, int]]:
    if k <= 0:
        return []
    items = list(freqs.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    return items[:k]

def merge_freqs(maps: List[Dict[str, int]]) -> Dict[str, int]:
    merged_freqs = Counter()
    for freq_map in maps:
        merged_freqs.update(freq_map)
    return dict(merged_freqs)

if __name__ == "__main__":
    tokens1 = ["яблоко", "банан", "яблоко", "апельсин", "банан", "яблоко", "киви", "груша"]
    freqs1 = count_tokens(tokens1)
    print("--- 1. count_tokens ---")
    print(f"Токены: {tokens1}")
    print(f"Частоты: {freqs1}")

    print("\n--- 2. top_k (с сортировкой) ---")
    k = 3
    top_3 = top_k(freqs1, k)
    print(f"Топ {k} токенов: {top_3}")
    
    freqs_tie = {"собака": 3, "кот": 3, "муравей": 2, "белка": 2}
    k_tie = 3
    top_k_tie = top_k(freqs_tie, k_tie)
    print(f"\nТест ничьей (k={k_tie}): {freqs_tie}")
    print(f"Результат: {top_k_tie}")

    k_zero = 0
    top_k_zero = top_k(freqs1, k_zero)
    print(f"\nТест k={k_zero}: {top_k_zero}")

    print("\n--- 3. merge_freqs (опционально) ---")

    map_a = {"a": 2, "b": 1, "c": 5}
    map_b = {"a": 3, "d": 4, "c": 2}
    merged = merge_freqs([map_a, map_b, freqs1])
    print(f"Map A: {map_a}")
    print(f"Map B: {map_b}")
    print(f"Объединенный результат: {merged}")

