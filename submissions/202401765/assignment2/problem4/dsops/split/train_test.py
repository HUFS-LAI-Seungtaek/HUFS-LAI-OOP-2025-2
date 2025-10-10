import random
from typing import List, Tuple


# train_test_split 함수 코드 제미나이 도움 받음
def train_test_split(seq: List, test_ratio: float, seed: int | None = None) -> Tuple[List, List]:
    """
    Splits a sequence into train and test sets.
    """
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("Test ratio must be between 0.0 and 1.0")

    data = list(seq)


    # 시드 설정부분 제미나이 도움받음
    if seed is not None:
        random.seed(seed)
    
    random.shuffle(data)
    
    test_size = int(round(len(data) * test_ratio))
    train_size = len(data) - test_size
    
    return data[:train_size], data[train_size:]


# 테스트 코드 제미나이 도움 받음
if __name__ == "__main__":
    def run_tests():
        # Example from README
        train, test = train_test_split([1,2,3,4,5], test_ratio=0.4, seed=42)
        assert len(train) == 3
        assert len(test) == 2
        
        # Instructor's test
        train, test = train_test_split(list(range(5)), 0.4, seed=0)
        assert train == [1, 4, 3]
        assert test == [2, 0]

        try:
            train_test_split([1,2,3], test_ratio=1.5)
            assert False, "ValueError was not raised for test_ratio > 1.0"
        except ValueError:
            print("train_test_split tests passed.")

    run_tests()
