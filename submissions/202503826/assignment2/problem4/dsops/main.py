if __name__ == "__main__":
    from .split.train_test import train_test_split
    from .stats.labels import label_distribution

    tr, te = train_test_split([1, 2, 3, 4, 5], 0.4, seed=42)
    print(tr, te)
    print(label_distribution(["cat", "dog", "cat"]))
