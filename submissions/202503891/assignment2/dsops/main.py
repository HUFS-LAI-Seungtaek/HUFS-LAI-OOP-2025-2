
if __name__ == "__main__":
    from . import train_test_split, label_distribution
    
    tr, te = train_test_split([1, 2, 3, 4, 5], test_ratio=0.4, seed=42)
    print("Train:", tr)
    print("Test:", te)
    
    dist = label_distribution(["cat", "dog", "cat"])
    print("Label distribution:", dist)
