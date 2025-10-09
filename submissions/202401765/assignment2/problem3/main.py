import collections
from typing import List, Dict, Tuple

def count_tokens(tokens: List[str]) -> Dict[str, int]:
    """
    Count token frequencies from a list of tokens.
    """
    return collections.Counter(tokens)

# 토큰 추출하는 코드 제미나이 도움 받음

def top_k(freqs: Dict[str, int], k: int) -> List[Tuple[str, int]]:
    """
    Get top-k most frequent tokens.
    Sorted by frequency (desc) and token name (asc) for ties.
    Returns empty list for k <= 0.
    """
    if k <= 0:
        return []
    
    # 정렬 기준: 빈도는 내림차순(-freq), 토큰은 오름차순
    sorted_items = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_items[:k]

# 딕셔너리 병합하는 코드 제미나이 도움 받음

def merge_freqs(maps: List[Dict[str, int]]) -> Dict[str, int]:
    """
    Merge multiple frequency dictionaries.
    """
    result = collections.defaultdict(int)
    for freq_dict in maps:
        for key, value in freq_dict.items():
            result[key] += value
    return dict(result)


if __name__ == "__main__":
    def run_tests():
        # count_tokens test
        assert count_tokens(["a","b","a"]) == {"a":2,"b":1}


        # top_k 함수 조건 처리부분 제미나이 도움 받음
        
        # top_k test
        assert top_k({"a":2,"b":2,"c":1}, 2) == [("a",2),("b",2)]
        assert top_k({"a":2, "b":1, "c":3}, 2) == [("c",3), ("a",2)]
        assert top_k({"a":2, "b":1, "c":3}, 0) == []

        # merge_freqs test
        assert merge_freqs([{"a":1},{"a":2,"b":1}]) == {"a":3,"b":1}
        assert merge_freqs([{"a":1, "b":1}, {"b":1, "c":1}]) == {"a":1, "b":2, "c":1}

        print("All Problem 3 tests passed.")

    run_tests()
