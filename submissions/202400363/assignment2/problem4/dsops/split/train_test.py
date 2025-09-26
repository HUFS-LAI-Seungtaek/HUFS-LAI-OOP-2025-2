
import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    # 1. test_ratio 유효성 검사
    if not 0.0 <= test_ratio <= 1.0:
        raise ValueError("test_ratio must be between 0.0 and 1.0")
    
    # 2. 원본 보존을 위해 리스트 복사
    copied_seq = list(seq)

    # 3. 시드가 있으면 random.seed()로 셔플 고정
    if seed is not None:
        random.seed(seed)
    random.shuffle(copied_seq)

    # 4. 분할할 인덱스 계산
    split_index = int(round(len(copied_seq) * (1 - test_ratio)))

    # 5. 분할하여 반환
    train_set = copied_seq[:split_index]
    test_set = copied_seq[split_index:]
    
    return train_set, test_set