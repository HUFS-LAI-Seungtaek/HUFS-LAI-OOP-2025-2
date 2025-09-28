from collections import Counter
from typing import List, Dict


from collections import Counter
from typing import List, Dict

def label_distribution(labels: List[str]) -> Dict[str, int]:
    return dict(Counter(labels))