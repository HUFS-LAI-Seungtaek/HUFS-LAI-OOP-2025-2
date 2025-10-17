import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    """
    주어진 리스트를 훈련 세트와 테스트 세트로 나눕니다.
    """
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0.")

    if not seq:
        return [], []

    copied_seq = seq.copy()

    if seed is not None:
        random.seed(seed)
    random.shuffle(copied_seq)

    cut_index = int(round(len(copied_seq) * (1 - test_ratio)))

    train = copied_seq[:cut_index]
    test = copied_seq[cut_index:]

    return train, test