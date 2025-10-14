import random
# 원본 불변을 지키기 위한 복사의 방법을 진행하는 과정에서 gpt의 도움을 받았습니다.
def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    
    if test_ratio > 1.0 or test_ratio < 0.0:
        raise ValueError
    
    if test_ratio == 0.0:
        test = []
    elif test_ratio == 1.0:
        train = []

    copy = seq[:]
    random.seed(seed)
    random.shuffle(copy)
    cut = int(round(len(seq) * (1 - test_ratio)))
    train = copy[:cut]
    test = copy[cut:]

    return train, test