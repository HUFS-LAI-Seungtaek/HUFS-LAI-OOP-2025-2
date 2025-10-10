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
    s = re.sub(r"\s+", " ", s) # perplexity의 도움을 받은 부분. 정규표현식에 익숙하지 않아 코드 구현에 도움을 받음.
    s = s.strip()
    keep = {"'", "-"}
    remove = set(string.punctuation) - keep
    s = ''.join(ch for ch in s if ch not in remove)
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