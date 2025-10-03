def label_distribution(labels: list[str]) -> dict[str, int]:
    result = {}
    for label in labels:
        result[label] = result.get(label, 0) + 1
    
    return result