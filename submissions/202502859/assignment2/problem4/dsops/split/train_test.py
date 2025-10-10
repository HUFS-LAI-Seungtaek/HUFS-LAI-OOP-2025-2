# dsops/split/train_test.py

import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    """
    주어진 시퀀스를 학습(train) 및 테스트(test) 세트로 나누는 함수입니다.
    """
    
    # 1. 입력 비율 검증 (Edge Case)
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio는 0.0과 1.0 사이여야 합니다.")

    # 2. 입력 복사, 시드 설정 및 셔플 (원본 불변 규칙)
    shuffled_seq = seq[:] # 입력 리스트 복사
    
    if seed is not None:
        random.seed(seed) # 시드가 있으면 난수 생성기 고정
    
    random.shuffle(shuffled_seq) # 복사본 셔플

    # 3. 컷 인덱스 계산
    seq_len = len(shuffled_seq)
    
    # train_size를 계산. (1 - test_ratio)를 곱하고 round 처리
    train_size = int(round(seq_len * (1.0 - test_ratio)))
    
    # 4. 분할하여 반환
    train_set = shuffled_seq[:train_size]
    test_set = shuffled_seq[train_size:]
    
    # Edge cases (test_ratio=0.0/1.0, 빈 입력)은 이 로직으로 자연스럽게 처리됨
    return train_set, test_set