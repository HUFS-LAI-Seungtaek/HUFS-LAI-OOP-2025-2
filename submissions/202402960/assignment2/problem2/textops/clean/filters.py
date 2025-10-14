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
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    keep = {"'","-"}
    remove_punct = set(string.punctuation) - keep
    result=""
    for ch in s:
        if ch not in remove_punct:
            result += ch
    return result 

#17~21 코드는 chatGPT의 도움을 받았습니다


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()