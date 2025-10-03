from . import train_test_split, label_distribution

if __name__ == "__main__":
    def run_demo():
        # A simple main to demo and test the package
        tr, te = train_test_split([1, 2, 3, 4, 5], 0.4, seed=42)
        print("Train/Test Split:", tr, te)
        
        label_dist = label_distribution(["cat", "dog", "cat"])
        print("Label Distribution:", label_dist)

    run_demo()