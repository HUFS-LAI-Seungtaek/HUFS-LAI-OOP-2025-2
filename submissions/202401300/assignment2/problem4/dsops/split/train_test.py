import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0 and 1")
    
    data = seq[:]
    if seed is not None:
        random.seed(seed)
    random.shuffle(data)
    
    cut = int(round(len(data) * (1 - test_ratio)))
    train = data[:cut]
    test = data[cut:]
    return train, test

print(train_test_split(list(range(5)), 0.4, seed=0))