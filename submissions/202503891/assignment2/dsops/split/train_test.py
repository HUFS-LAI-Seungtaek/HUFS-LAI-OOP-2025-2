import random
from typing import List, Tuple, Optional

def train_test_split(seq: List, test_ratio: float, seed: Optional[int] = None) -> Tuple[List, List]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")
    
    seq_copy = seq[:]  # 원본 보존
    
    if seed is not None:
        random.seed(seed)
    
    random.shuffle(seq_copy)
    
    cutoff = int(round(len(seq_copy) * (1 - test_ratio)))
    train = seq_copy[:cutoff]
    test = seq_copy[cutoff:]
    
    return train, test
