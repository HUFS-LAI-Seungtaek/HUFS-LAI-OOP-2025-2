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

'''credit:train_test_split 함수를 구현하면서, 리스트를 재현 가능한 방식으로 섞어
train/test로 나누는 방법에 대해 gpt에게 도움을 받았습니다.'''
