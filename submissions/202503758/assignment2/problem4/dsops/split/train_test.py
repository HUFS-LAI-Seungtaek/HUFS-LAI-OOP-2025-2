import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0): raise ValueError()
    if not seq: return [], []
    
    copy = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy)

    idx = int(round(len(seq) * (1 - test_ratio)));
    train_set, test_set = copy[:idx], copy[idx:]

    return train_set, test_set

