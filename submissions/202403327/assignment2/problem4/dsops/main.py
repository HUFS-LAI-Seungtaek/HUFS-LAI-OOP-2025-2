from dsops import train_test_split, label_distribution
if __name__ == "__main__":
    print("--- train_test_split Demo ---")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    train, test = train_test_split(data, test_ratio=0.3, seed=42)
    print(f"Original data: {data}")
    print(f"Train set: {train}")
    print(f"Test set:  {test}")

    print("\n--- label_distribution Demo ---")
    labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
    dist = label_distribution(labels)
    print(f"Labels: {labels}")
    print(f"Distribution: {dist}")
"""
(도움받은 내용):
dsops 패키지를 처음부터 직접 구현하는 과정에서 생성형 AI(Gemini)의 도움을 받았습니다.
- train_test_split: random.seed()를 통한 재현성 확보, 원본 데이터 보존을 위한 리스트 복사, 데이터 분할 로직 구현에 도움을 받았습니다.
- label_distribution: 이전 문제의 패턴을 재활용하여 구현했습니다.
"""