def label_distribution(labels: list[str]) -> dict[str, int]:
	dist = {}
	for label in labels:
		dist[label] = dist.get(label, 0) + 1
	return dist
    