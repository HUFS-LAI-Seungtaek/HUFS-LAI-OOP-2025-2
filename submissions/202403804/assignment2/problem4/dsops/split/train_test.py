import random

def train_test_split(
    seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    #검증: `0.0 <= test_ratio <= 1.0` 아니면 `ValueError`
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio는 0.0과 1.0 사이여야 한다.")
    
    #구현:
    # 입력을 복사해 셔플(원본 보존)
    # `seed`가 주어지면 `random.seed(seed)` 후 `random.shuffle(copy)`
    shuffled_seq = seq.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(shuffled_seq)
    
    #컷 인덱스 = `int(round(len(seq) * (1 - test_ratio)))`
    #앞부분 = train, 뒷부분 = test로 잘라 반환
    cut_index = int(round(len(seq) * (1 - test_ratio)))
    train = shuffled_seq[:cut_index]
    test = shuffled_seq[cut_index:]
    return train, test