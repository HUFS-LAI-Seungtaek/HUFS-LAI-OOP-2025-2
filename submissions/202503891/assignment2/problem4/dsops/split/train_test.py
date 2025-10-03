import random
from typing import List, Tuple, Optional

def train_test_split(seq: List, test_ratio: float, seed: Optional[int] = None) -> Tuple[List, List]:
    if not 0 <= test_ratio <= 1:
        raise ValueError("test_ratio must be between 0 and 1")

    copy_seq = seq[:]
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy_seq)

    cut = int(round(len(copy_seq) * (1 - test_ratio)))
    train = copy_seq[:cut]
    test = copy_seq[cut:]
    return train, test
