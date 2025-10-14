import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0<= test_ratio <= 1):
        raise ValueError("테스트 데이터의 비율은 0과 1 사이여야 합니다.")

    copy = seq.copy()
    if seed is not None:
        random.seed(seed)
        random.shuffle(copy)
    #random 함수 사용법을 ChatGPT를 통해 이해하고 사용하였습니다.

    if test_ratio == 0.0:
        return copy[:], []
    elif test_ratio == 1.0:
        return [], copy[:]
    elif len(seq) == 0:
        return [], []
    else:
        cut_index = int(round(len(seq) * (1 - test_ratio)))
        train = copy[:cut_index]
        test = copy[cut_index:]
        return train, test

