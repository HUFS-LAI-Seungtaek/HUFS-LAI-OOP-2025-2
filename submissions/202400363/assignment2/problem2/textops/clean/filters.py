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
    s=s.lower() 
    #s=re.sub(r"\s+", " ", s)
    #s=s.strip() 
    # 4) string.punctuation에서 특정 문자 제외하고 제거
    # 5) set 연산을 활용해서 keep = {"'", "-"}, 나머지는 제거
    remove_punctuation = string.punctuation.replace("'", "").replace("-", "")
    translator = str.maketrans("", "", remove_punctuation)
    s = s.translate(translator)
    s=s.strip()
    s=re.sub(r"\s+", " ", s)
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