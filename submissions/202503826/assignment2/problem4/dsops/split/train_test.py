import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    copy_seq = seq.copy()
    if not seq:
        return [], []
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy_seq)
    if not (0 <= test_ratio <= 1):
        raise ValueError("ValueError")
    cut = int(len(copy_seq) * test_ratio)  #컷 인덱스 부분 GPT 참조
    train = copy_seq[:cut]
    test = copy_seq[cut:]
    return train, test