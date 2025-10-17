from . import train_test_split, label_distribution  

if __name__ == "__main__":
    tr, te = train_test_split([1, 2, 3, 4, 5], test_ratio=0.4, seed=42)
    print("train:", tr)
    print("test :", te)

    dist = label_distribution(["cat", "dog", "cat"])
    print("dist :", dist)
