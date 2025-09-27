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
    # 1) 소문자로 변환
    s = s.lower()
    
    # 2) 앞뒤 공백 제거
    s = s.strip()
    
    # 3) 모든 연속 공백을 하나로
    s = re.sub(r"\s+", " ", s)
    
    # 4) 아포스트로피(')와 하이픈(-)만 남기고 나머지 구두점 제거
    keep = {"'", "-"}
    remove_punct = "".join(ch for ch in string.punctuation if ch not in keep)
    s = s.translate(str.maketrans("", "", remove_punct))

    return s

if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
    pass