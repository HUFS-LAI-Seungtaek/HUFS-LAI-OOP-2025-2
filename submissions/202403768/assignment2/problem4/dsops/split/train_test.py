import random
from typing import List, Tuple

def train_test_split(seq: List, test_ratio: float, seed: int | None = None) -> Tuple[List, List]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0.")
    
    data = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(data)
    
    cut_idx = int(round(len(data) * (1 - test_ratio)))
    
    train = data[:cut_idx]
    test = data[cut_idx:]
    
    return train, test