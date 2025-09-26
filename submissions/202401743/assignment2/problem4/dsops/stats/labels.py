import collections
from typing import List,Dict

def label_distribution(labels: List[str]) -> Dict[str, int]:
    if not isinstance(labels, list):
        raise TypeError("labels must be a list")
    return dict(collections.Counter(labels))

if __name__ == "__main__":
    print(label_distribution(["cat","dog","cat"]))