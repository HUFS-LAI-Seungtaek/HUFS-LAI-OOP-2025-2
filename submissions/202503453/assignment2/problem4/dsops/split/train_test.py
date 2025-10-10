import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0 and 1")

    
    if not seq:
        return [], []

    
    seq_copy = seq.copy()

    if seed is not None:
        random.seed(seed)

    random.shuffle(seq_copy)

    
    cut = int(round(len(seq_copy) * (1 - test_ratio)))

    train = seq_copy[:cut]
    test = seq_copy[cut:]
    return train, test
