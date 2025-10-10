def label_distribution(labels: list[str]) -> dict[str, int]:
    freq = {}
    for label in labels:
        freq[label] = freq.get(label, 0) + 1 # perplexity의 도움을 받은 부분. get 메소드를 열심히 활용해야 함을 깨달았다.
    return freq