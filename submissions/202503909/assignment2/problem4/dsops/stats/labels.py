from typing import List, Dict
from collections import Counter

def label_distribution(labels: List[str]) -> Dict[str, int]:

    return dict(Counter(labels))


if __name__ == "__main__":
    def run_tests():
        assert label_distribution(["a", "b", "a"]) == {"a": 2, "b": 1}
        assert label_distribution([]) == {}
        print("labels.py tests passed.")
    run_tests()