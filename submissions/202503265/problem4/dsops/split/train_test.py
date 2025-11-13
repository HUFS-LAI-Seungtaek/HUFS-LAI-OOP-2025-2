import random

def train_test_split(
    seq: list, test_ratio: float, seed: int | None = None
) -> tuple[list, list]:
    """
    주어진 시퀀스를 훈련 세트와 테스트 세트로 나눕니다.
    원본 리스트는 변경하지 않습니다.
    """

    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0.")
    data_copy = seq.copy()

    if seed is not None:
        random.seed(seed)
    random.shuffle(data_copy)

    split_index = int(round(len(data_copy) * (1 - test_ratio)))

    train_set = data_copy[:split_index]
    test_set = data_copy[split_index:]

    return train_set, test_set