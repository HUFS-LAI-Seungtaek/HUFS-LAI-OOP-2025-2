import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not 0.0 <= test_ratio <= 1.0:
        raise ValueError("invalid ratio")
    n = len(seq)
    if n == 0:
        return [], []
    data = list(seq)
    if seed is not None:
        random.seed(seed)
    random.shuffle(data)
    cut = int(round(n * (1 - test_ratio)))
    return data[:cut], data[cut:]