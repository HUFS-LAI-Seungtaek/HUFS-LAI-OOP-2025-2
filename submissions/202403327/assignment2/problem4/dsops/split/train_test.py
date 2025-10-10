import random
def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")
    if seed is not None:
        random.seed(seed)
    seq_copy = seq.copy()
    random.shuffle(seq_copy)
    cut_idx = int(round(len(seq_copy) * (1 - test_ratio)))
    train_set = seq_copy[:cut_idx]
    test_set = seq_copy[cut_idx:]

    return train_set, test_set