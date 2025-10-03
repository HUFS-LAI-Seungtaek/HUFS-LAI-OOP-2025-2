import random
import copy

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio는 0.0과 1.0 사이여야 합니다.")

    data_copy = copy.deepcopy(seq)
    n = len(data_copy)

    if seed is not None:
        random.seed(seed)
    
    random.shuffle(data_copy)

    cut_index = int(round(n * (1.0 - test_ratio)))

    train_set = data_copy[:cut_index]
    test_set = data_copy[cut_index:]

    return train_set, test_set
