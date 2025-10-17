from dsops import train_test_split, label_distribution

def run_demo():
    """패키지 기능 시연 함수"""
    print("--- train_test_split 데모 ---")
    data = list(range(1, 11)) 
    
    train, test = train_test_split(data, test_ratio=0.3, seed=42)
    
    print(f"원본 데이터 ({len(data)}개): {data}")
    print(f"Train 세트 ({len(train)}개): {train}") 
    print(f"Test 세트 ({len(test)}개): {test}")   
    
    print("\n--- label_distribution 데모 ---")
    labels = ["cat", "dog", "cat", "dog", "cat", "bird"]
    dist = label_distribution(labels)
    print(f"라벨 분포: {dist}")

if __name__ == "__main__":
    run_demo()