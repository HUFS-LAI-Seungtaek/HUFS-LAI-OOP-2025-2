if __name__ == "__main__":
    from . import train_test_split, label_distribution

    data = [1, 2, 3, 4, 5]
    train, test = train_test_split(data, test_ratio=0.4, seed=42)
    print("Train:", train)
    print("Test:", test)

    labels = ["cat", "dog", "cat"]
    print("Label distribution:", label_distribution(labels))
