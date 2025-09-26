if __name__ == "__main__":
    from . import train_test_split, label_distribution
    
    print("--- train_test_split 테스트 ---")
    tr, te = train_test_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0.4, seed=42)
    print(f"Train set: {tr}")
    print(f"Test set: {te}")
    print("-" * 20)
    
    print("--- label_distribution 테스트 ---")
    labels = ["cat", "dog", "cat", "fish", "dog", "cat"]
    distribution = label_distribution(labels)
    print(f"Label distribution: {distribution}")
    print("-" * 20)

    print("--- 엣지 케이스 테스트 ---")
    try:
        tr_invalid, te_invalid = train_test_split([1, 2, 3], 1.1)
    except ValueError as e:
        print(f"ValueError caught: {e}")
    
    tr_all, te_all = train_test_split([1, 2, 3], 1.0)
    print(f"Ratio 1.0: {tr_all}, {te_all}")
    
    tr_none, te_none = train_test_split([1, 2, 3], 0.0)
    print(f"Ratio 0.0: {tr_none}, {te_none}")