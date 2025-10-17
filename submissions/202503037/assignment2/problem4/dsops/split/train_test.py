import random

def train_test_split(seq: list, test_ratio: float, seed: int = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")
    if len(seq) == 0:
        return [], []
    copy = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy)
    train = copy[:int(round(len(seq) * (1 - test_ratio)))]
    test = copy[int(round(len(seq) * (1 - test_ratio))):]
    return train, test