from typing import List, Dict

def label_distribution(labels: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for label in labels:
        result[label] = result.get(label, 0) + 1
    return result
