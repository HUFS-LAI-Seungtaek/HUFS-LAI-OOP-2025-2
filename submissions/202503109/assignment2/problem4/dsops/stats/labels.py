def label_distribution(labels: list[str]) -> dict[str, int]:
    """
    Return a frequency dictionary for given label list.
    """
    freq: dict[str, int] = {}
    for lb in labels:
        freq[lb] = freq.get(lb, 0) + 1
    return freq


if __name__ == "__main__":
    assert label_distribution(["a","b","a"]) == {"a": 2, "b": 1}
