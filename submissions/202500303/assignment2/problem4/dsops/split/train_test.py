import random
import math

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    copy = list(seq)
    #edge cases
    if test_ratio < 0 or test_ratio > 1:
        raise ValueError("test_ratio must be between 0 and 1")
    if len(copy) == 0:
        return [], []
    if math.isclose(test_ratio, 0.0): #처음 if test_ratio == 1.0,  float 타입 오류 가능성 때문에 수정함 (gpt)
        return copy, []
    if math.isclose(test_ratio, 1.0): 
        return [], copy
    #shuffle
    if seed is not None: 
        random.seed(seed)
        random.shuffle(copy)
    #split
    cut_index = int(round(len(copy) * (1 - test_ratio)))
    train = copy[:cut_index]
    test = copy[cut_index:]
    return train, test

    