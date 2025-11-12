def label_distribution(labels: list[str]) -> dict[str, int]:
    dict_labels = {}
    for label in labels:
        dict_labels[label] = dict_labels.get(label, 0) + 1
    return dict_labels