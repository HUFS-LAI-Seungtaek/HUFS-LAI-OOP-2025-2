import re
import string

def clean_text(s: str) -> str:
    """
    Pipeline:
      1) lowercase
      2) strip
      3) collapse all whitespace to single spaces
      4) remove ASCII punctuation except apostrophes (') and hyphens (-)
    """
    # TODO: 구현하세요
    # 힌트:
    # 1) s.lower() - 소문자 변환
    # 2) re.sub(r"\s+", " ", s) - 모든 연속 공백을 단일 공백으로
    # 3) s.strip() - 앞뒤 공백 제거
    # 4) string.punctuation에서 특정 문자 제외하고 제거 
    # 5) set 연산을 활용해서 keep = {"'", "-"}, 나머지는 제거
    # regular expression module
    s = s.lower()
    s = s.strip()
    s = re.sub(r"\s+", " ", s) #입력 s에서-하나이상의(+)공백(str)을(\s)-단일공백(" ")으로 substitute
    keep = {"'", "-"}
    punctuation_to_remove = set(string.punctuation) - keep
    pattern_to_remove = f"[{re.escape(''.join(punctuation_to_remove))}]" 
    s = re.sub(pattern_to_remove, "", s)
    #credits for regular expression module: https://cdragon.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D%EA%B3%BC-re%EB%AA%A8%EB%93%88-%EC%82%AC%EC%9A%A9%EB%B2%95
    #보다 간결한 방법에 대해, 또는 re module에 대해 식견이 있으신 분들의 과감한 피드백을 부탁드립니다!
    return s
    
    


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
    