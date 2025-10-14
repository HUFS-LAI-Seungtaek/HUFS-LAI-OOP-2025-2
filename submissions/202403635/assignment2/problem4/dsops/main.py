# 생성형 AI Gemini 사용범위: 코드 초안 생성, 파이썬 특정 기능과 코드 제안 및 설명 (코드 제안 시 같은 줄에 명시), 작성한 코드 리뷰 요청
if __name__ == "__main__":
    from . import train_test_split, label_distribution

    print("--- dsops package demonstration ---")

# 아래 테스트 부분 코드를 생성형 AI Gemini를 통해 제안받고 상세한 설명을 요청했습니다.
    # 1. train_test_split 함수 테스트
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    train, test = train_test_split(data, test_ratio=0.3, seed=42)
    
    print(f"\nOriginal data: {data}")
    print(f"Train set (seed=42): {train}")
    print(f"Test set (seed=42):  {test}")

    # 2. label_distribution 함수 테스트
    labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
    distribution = label_distribution(labels)

    print(f"\nLabels: {labels}")
    print(f"Label Distribution: {distribution}")

    print("\n--- Demonstration finished ---")