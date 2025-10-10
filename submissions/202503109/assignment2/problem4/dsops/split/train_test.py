import random
from typing import Tuple, List, Any

#학습을 위해 AI 사용 후 주석을 남겨둠
def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    """
    Split a list into train/test by test_ratio.
    - Validates 0.0 <= test_ratio <= 1.0 (else ValueError)
    - Shuffles a copy (original list remains unchanged)
    - If seed is provided, sets random.seed(seed) before shuffle
    - Cut index = int(round(len(seq) * (1 - test_ratio)))
    """
    if not (0.0 <= float(test_ratio) <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")

    data = list(seq)  # copy to keep original intact

    if seed is not None:
        random.seed(seed)
    random.shuffle(data)

    cut = int(round(len(data) * (1 - test_ratio)))
    train = data[:cut]
    test = data[cut:]
    return train, test


if __name__ == "__main__":
    # quick self-test (no prints required by spec; this is optional)
    tr, te = train_test_split([1,2,3,4,5], 0.4, seed=42)
    assert isinstance(tr, list) and isinstance(te, list)
