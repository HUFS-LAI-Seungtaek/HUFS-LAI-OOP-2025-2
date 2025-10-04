import random


def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <=1.0):
        raise ValueError("test_ratio는 0.0과 1.0 사이의 값이어야 합니다.")
    
    copy = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy)

    cut = int(round(len(seq) * (1 - test_ratio)))
    return copy[:cut], copy[cut:]