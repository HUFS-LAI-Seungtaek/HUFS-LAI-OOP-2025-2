def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    copy_seq = seq.copy()
    if not seq:
        return [], []
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy_seq)

#권희원 학우의 도움을 받았습니다.
