import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError
    n = len(seq)
    if n == 0:
        return [], []
    seq_copy = seq.copy() # perplexity의 도움을 받은 부분. 단순히 복사하는 좋은 메소드를 새로이 알았다.
    if seed is not None:
        random.seed(seed)
    random.shuffle(seq_copy)
    cut = int(round(n * (1 - test_ratio)))
    train = seq_copy[:cut]
    test = seq_copy[cut:]
    return train, test