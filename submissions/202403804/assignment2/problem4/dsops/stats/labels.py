def label_distribution(labels: list[str]) -> dict[str, int]:
    label_list = {}
    for label in labels:
        label_list[label] = label_list.get(label, 0) + 1
    return label_list
