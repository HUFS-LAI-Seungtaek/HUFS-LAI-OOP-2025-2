import random
#from typing import List, Tuple, Any, Optional
#def train_test_split(seq: list, test_ratio: float, seed: Optional[int]) -> tuple[list, list]:
def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError
    data_copy = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(data_copy)
    n = len(data_copy)
    train_size = int(round(n * (1.0 - test_ratio)))
    train = data_copy[:train_size]
    test = data_copy[train_size:]
    return train, test

# 2-3 : python 버전차이로 실행이 어려워 Gemini참고하여 수정 후 데모 실행 하였습니다.