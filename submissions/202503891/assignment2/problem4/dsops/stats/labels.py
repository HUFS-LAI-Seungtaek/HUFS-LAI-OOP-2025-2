from typing import List, Dict

def label_distribution(labels: List[str]) -> Dict[str, int]:
    freq = {}
    for label in labels:
        freq[label] = freq.get(label, 0) + 1
    return freq
