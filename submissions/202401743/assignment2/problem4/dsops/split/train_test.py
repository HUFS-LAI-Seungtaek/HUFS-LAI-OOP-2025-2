import random
from typing import List, Tuple, Optional, Any

def train_test_split(seq: List[Any], test_ratio: float, seed: Optional[int] = None) -> Tuple[List[Any], List[Any]]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0, inclusive.")
    shuffled_seq = list(seq)
    if seed is not None:
        random.seed(seed)
    random.shuffle(shuffled_seq)
    seq_len = len(seq)
    train_end_index = int(round(seq_len * (1.0 - test_ratio)))
    train_set = shuffled_seq[:train_end_index]
    test_set = shuffled_seq[train_end_index:]
    return train_set, test_set

if __name__ == "__main__":
    print(train_test_split(list(range(5)), 0.4, seed = 0))