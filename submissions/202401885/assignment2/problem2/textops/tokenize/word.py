import re
from typing import List

def word_tokens(s: str) -> List[str]:
    """
    규칙:
    - 단일 공백 기준 분할
    - 빈 문자열/공백뿐이면 [] 반환
    - 입력이 비정규화여도 안전하게 동작하도록 내부적으로 공백 축약 후 split
    """
    if not isinstance(s, str):
        raise TypeError("word_tokens: input must be str")

    s = re.sub(r"\s+", " ", s).strip()
    if not s:
        return []
    return s.split(" ")
