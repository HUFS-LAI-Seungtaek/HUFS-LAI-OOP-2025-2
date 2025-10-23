# textops/clean/filters.py

import re
import string
from typing import Set

def clean_text(s: str) -> str:
    """
    주어진 문자열을 정규화합니다.
    Pipeline:
      1) lowercase
      2) remove ASCII punctuation except apostrophes (') and hyphens (-)
      3) collapse all whitespace to single spaces
      4) strip leading/trailing whitespace
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # 1. 소문자 변환
    s = s.lower()

    # 2. 유지할 문장 부호를 제외한 나머지 제거
    # str.maketrans 대신 replace와 반복문 사용
    punctuation_to_keep: Set[str] = {"'", "-"}
    
    # 지워야 할 문장 부호 목록을 순회하며 하나씩 제거
    for char in string.punctuation:
        if char not in punctuation_to_keep:
            s = s.replace(char, "")

    # 3. 모든 연속 공백(스페이스, 탭, 개행 등)을 단일 공백으로 축약
    # 정규식 re.sub 대신 replace와 while 반복문 사용
    
    # 탭과 개행 문자를 먼저 일반 공백으로 바꿈
    s = s.replace('\n', ' ')
    s = s.replace('\t', ' ')

    # 연속된 두 개의 공백('  ')을 하나의 공백(' ')으로 바꿈
    # 더이상 '  '이 없을 때까지 반복
    while '  ' in s:
        s = s.replace('  ', ' ')

    # 4. 앞뒤 공백 최종제거
    s = s.strip()

    return s

# 테스트코드눈 그대로 유지
if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters_simple.py tests passed.")
    run_tests()