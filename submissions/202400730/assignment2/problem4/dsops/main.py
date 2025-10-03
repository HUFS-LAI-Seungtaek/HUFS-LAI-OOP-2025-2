
if __name__ == "__main__":
    # 패키지 내부에서 실행하므로 상대 경로 import를 사용합니다.
    from . import train_test_split, label_distribution
    
    print("--- train_test_split 데모 ---")
    data = list(range(10))
    print(f"원본 데이터: {data}")
    
    # 시드를 고정하여 항상 같은 결과가 나오는지 확인
    train, test = train_test_split(data, test_ratio=0.3, seed=42)
    print(f"seed=42 결과 -> train: {train}, test: {test}")

    train_no_seed, test_no_seed = train_test_split(data, test_ratio=0.3)
    print(f"seed 없음 결과 -> train: {train_no_seed}, test: {test_no_seed}")

    # Edge cases 테스트
    print("\n--- Edge Cases ---")
    print(f"test_ratio=0.0: {train_test_split(data, 0.0)}")
    print(f"test_ratio=1.0: {train_test_split(data, 1.0)}")
    print(f"빈 리스트: {train_test_split([], 0.5)}")

    print("\n--- label_distribution 데모 ---")
    labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
    distribution = label_distribution(labels)
    print(f"레이블: {labels}")
    print(f"분포: {distribution}")
