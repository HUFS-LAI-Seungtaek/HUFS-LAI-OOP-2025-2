'''
- 검증: `0.0 <= test_ratio <= 1.0` 아니면 `ValueError`
  - 구현:
    - 입력을 복사해 셔플(원본 보존)
    - `seed`가 주어지면 `random.seed(seed)` 후 `random.shuffle(copy)`
    - 컷 인덱스 = `int(round(len(seq) * (1 - test_ratio)))`
    - 앞부분 = train, 뒷부분 = test로 잘라 반환
'''
import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if test_ratio < 0.0 or test_ratio > 1.0:
        raise ValueError("Test ratio must be between 0.0 and 1.0")
    if seq == []:
        return ([], [])
    if seed != None:
        random.seed(seed)
    shuf_seq = seq.copy()
    random.shuffle(shuf_seq)
    cut_index = int(round(len(seq) * (1 - test_ratio)))
    train = shuf_seq[:cut_index]
    test = shuf_seq[cut_index:]
    return (train, test)
