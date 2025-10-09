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
    s = re.sub(r"\s+", " ", s).strip()
    keep = {"'", "-"}
    remove = "".join(ch for ch in string.punctuation if ch not in keep)
    s = s.translate(str.maketrans("", "", remove)) #Gemini의 도움을 받았습니다
    return s


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
    
