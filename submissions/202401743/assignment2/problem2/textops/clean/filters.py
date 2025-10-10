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
    s = s.lower()
    remove = set(string.punctuation) - {"'", "-"}
    pattern = "[" + re.escape("".join(remove)) + "]"
    s = re.sub(pattern, "", s)
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    return s
    
# 15-20 코드는 Gemini를 사용하여 구현했습니다.


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
