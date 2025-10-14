def label_distribution(labels: list[str]) -> dict[str, int]:
    label_dict = {}
    for i in labels:
        label_dict[i] = label_dict.get(i,0) + 1
    return label_dict