import random

def train_test_split(seq, test_ratio, seed=None):
    if not 0<=test_ratio<=1:
        raise ValueError 
    if not seq:
        return [],[]
    seq_copy=seq.copy()

    if seed is not None:
        random.seed(seed)

    random.shuffle(seq_copy)
    cut=int(round(len(seq_copy) * (1 - test_ratio)))

    train = seq_copy[:cut]
    test = seq_copy[cut:]

    return train,test