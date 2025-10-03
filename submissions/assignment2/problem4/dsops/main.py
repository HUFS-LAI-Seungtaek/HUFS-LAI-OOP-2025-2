"""
dsops 패키지 데모 실행 스크립트
"""

if __name__ == "__main__":
    # 상대경로로 패키지 함수들 가져오기
    from . import train_test_split, label_distribution
    
    print("=== dsops 패키지 데모 ===")
    
    # Train/Test Split 데모
    print("\n1. Train/Test Split 테스트:")
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    train_set, test_set = train_test_split(sample_data, test_ratio=0.4, seed=42)
    print(f"원본 데이터: {sample_data}")
    print(f"훈련 데이터: {train_set}")
    print(f"테스트 데이터: {test_set}")
    print(f"분할 비율: {len(test_set)}/{len(sample_data)} = {len(test_set)/len(sample_data):.1f}")
    
    # Label Distribution 데모
    print("\n2. Label Distribution 테스트:")
    sample_labels = ["cat", "dog", "cat", "bird", "dog", "cat", "fish"]
    distribution = label_distribution(sample_labels)
    print(f"레이블 리스트: {sample_labels}")
    print(f"분포 결과: {distribution}")
    
    # 재현성 테스트
    print("\n3. 재현성 테스트 (동일한 시드):")
    data1 = list(range(8))
    result1 = train_test_split(data1, 0.25, seed=100)
    result2 = train_test_split(data1, 0.25, seed=100)
    print(f"첫 번째 실행: {result1}")
    print(f"두 번째 실행: {result2}")
    print(f"결과 동일: {result1 == result2}")
    
    print("\n=== 데모 완료 ===")