import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0<= test_ratio <= 1):
        raise ValueError("테스트 데이터의 비율은 0과 1 사이여야 합니다.")

    if seed is not None:
        random.seed(seed)
        random.shuffle(seq)
    
    if test_ratio == 0.0:
        return seq[:], []
    elif test_ratio == 1.0:
        return [], seq[:]
    elif len(seq) == 0:
        return [], []
    else:
        cut_index = int(round(len(seq) * (1 - test_ratio)))
        train = seq[:cut_index]
        test = seq[cut_index:]
        return train, test

