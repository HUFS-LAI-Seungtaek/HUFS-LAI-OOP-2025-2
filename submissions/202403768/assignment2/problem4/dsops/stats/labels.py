from collections import Counter
from typing import List, Dict


from collections import Counter
from typing import List, Dict

def label_distribution(labels: List[str]) -> Dict[str, int]:
    return dict(Counter(labels))
case1 = ["cat", "dog", "cat", "bird", "cat"]
print(f"입력: {case1}")
print(f"결과: {label_distribution(case1)}")
# 예상 결과: {'cat': 3, 'dog': 1, 'bird': 1}
print("-" * 20)

case2 = []
print(f"입력: {case2}")
print(f"결과: {label_distribution(case2)}")
# 예상 결과: {}
print("-" * 20)

case3 = ["apple", "banana", "cherry"]
print(f"입력: {case3}")
print(f"결과: {label_distribution(case3)}")
# 예상 결과: {'apple': 1, 'banana': 1, 'cherry': 1}
print("-" * 20)