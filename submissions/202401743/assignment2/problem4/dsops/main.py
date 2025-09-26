if __name__ == "__main__":
    from . import train_test_split, label_distribution

    def run_demo():
        data = list(range(10))
        tr, te = train_test_split(data, test_ratio=0.4, seed=42)
        print(f"Train/Test Split (ratio 0.4, seed 42):")
        print(f"  Train: {tr}")
        print(f"  Test: {te}")
        
        labels = ["cat", "dog", "cat", "fish", "dog", "cat"]
        dist = label_distribution(labels)
        print(f"\nLabel Distribution Result:")
        print(dist)

        tr0, te0 = train_test_split(data, test_ratio=0.0)
        print(f"\nEdge Case (Ratio 0.0, Test size): {len(te0)}")
    run_demo()
    pass