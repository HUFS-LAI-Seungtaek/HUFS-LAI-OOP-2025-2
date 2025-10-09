from typing import Optional, Tuple, List
import random

def train_test_split(seq: List, test_ratio: float, seed: Optional[int] = None) -> Tuple[List, List]:
    
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")

    seq_copy = seq.copy()

    if seed is not None:
        random.seed(seed)
    random.shuffle(seq_copy)

    cut = int(round(len(seq) * (1 - test_ratio))) # Gemini의 도움을 받았습니다
    train = seq_copy[:cut]
    test = seq_copy[cut:]
    return train, test


if __name__ == "__main__":
    def run_tests():
        orig = [1, 2, 3, 4, 5]
        tr, te = train_test_split(orig, 0.4, seed=0)
        assert sorted(tr + te) == sorted(orig)
        assert orig == [1, 2, 3, 4, 5]
        assert train_test_split([], 0.5) == ([], [])
        assert train_test_split([1, 2], 0.0)[1] == []
        assert train_test_split([1, 2], 1.0)[0] == []
        try:
            train_test_split([1], -0.1)
            raise AssertionError("Expected ValueError for bad ratio")
        except ValueError:
            pass
        print("train_test.py tests passed.")
    run_tests()
    
