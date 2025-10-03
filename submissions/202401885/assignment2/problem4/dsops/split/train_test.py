import random
from typing import Tuple, List, Any

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    """
    리스트를 (train, test)로 분할한다.
    규칙:
      - 0.0 <= test_ratio <= 1.0 아니면 ValueError
      - 입력을 복사 후 셔플(원본 불변)
      - seed가 주어지면 random.seed(seed)로 고정
      - 컷 인덱스 = int(round(len(seq) * (1 - test_ratio)))
      - 앞: train, 뒤: test
    """
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0 and 1")

    data = list(seq)  # 원본 보존
    if seed is not None:
        random.seed(seed)
    random.shuffle(data)

    cut = int(round(len(data) * (1.0 - test_ratio)))
    train = data[:cut]
    test = data[cut:]
    return train, test
