def label_distribution(labels):
    labels_list={}
    for label in labels:
        labels_list[label]=labels_list.get(label,0)+1
    return labels_list