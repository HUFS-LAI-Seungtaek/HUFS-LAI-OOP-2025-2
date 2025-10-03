import collections
from typing import List, Dict

def label_distribution(labels: List[str]) -> Dict[str, int]:
    """
    Returns the distribution of labels.
    """
    return dict(collections.Counter(labels))

if __name__ == "__main__":
    def run_tests():
        assert label_distribution(["cat", "dog", "cat"]) == {"cat": 2, "dog": 1}
        assert label_distribution(["a", "b", "a"]) == {"a": 2, "b": 1}
        assert label_distribution([]) == {}
        print("label_distribution tests passed.")

    run_tests()