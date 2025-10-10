from typing import List, Dict
def label_distribution(labels: list[str]) -> dict[str, int]:
    freqs: dict[str, int]={}
    for lb in labels:
        freqs[lb] = freqs.get(lb, 0) + 1
    return freqs

print(label_distribution(["a", "b", "a"]))
    