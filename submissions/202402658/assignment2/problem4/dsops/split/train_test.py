import random


def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list] :
    """
    main work: cut the input sequence into train and test set.
    test ratio must be within [0.0 , 1.0]
    keep the original sequence aside safely, and use a copy for shuffling.
    if there's a seed on input, shuffle with that seed. else shuffle randomly.
    """

    if not 0.0 <= test_ratio <= 1.0 :
        raise ValueError('ValueError')

    if len(seq) == 0 :
        return [], []

    copy = seq[:]    #원본 보존, shuffle할 copy생성.

    if seed is not None:
        random.seed(seed)

    random.shuffle(copy)
    cut_idx = int(round(len(copy) * (1 - test_ratio)))
    train , test = copy[:cut_idx] , copy[cut_idx:]

    return train , test