# dsops/main.py

# 패키지 내에서 임포트할 때는 . 을 사용한 상대 경로 임포트를 권장
from . import train_test_split, label_distribution 

def run_demo():
    print("--- Problem 4 dsops Demo ---")
    
    # Instructor quick test 예시 포함
    print("1. Instructor Quick Test:")
    print(f"Split (Seed 0): {train_test_split(list(range(5)), 0.4, seed=0)}")   
    print(f"Distribution: {label_distribution(['a','b','a'])}") 
    
    print("\n2. General Demo:")
    data = [1,2,3,4,5]
    labels = ["cat","dog","cat"]
    
    tr, te = train_test_split(data, 0.4, seed=42)
    print(f"Split (Seed 42): Train={tr}, Test={te}") # 재현 가능한 분할 확인
    
    dist = label_distribution(labels)
    print(f"Distribution: {dist}") # {'cat':2,'dog':1}

    # 3. Edge Case: 비율 검증 (주석 처리 - 직접 테스트해야 함)
    # try:
    #     train_test_split(data, 1.1)
    # except ValueError as e:
    #     print(f"ValueError caught: {e}")
        
    # Edge Case: 100% test
    tr_full, te_full = train_test_split([1,2], 1.0)
    print(f"\nEdge Case (100% test): Train={tr_full}, Test={te_full}") 


if __name__ == "__main__":
    run_demo()