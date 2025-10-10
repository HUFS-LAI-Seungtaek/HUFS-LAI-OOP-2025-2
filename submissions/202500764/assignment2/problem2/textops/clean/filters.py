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
if not isinstance(s, str):
    raise TypeError("clean_text: 문자열 넣으세요.")
    s = s.lower()
    keep = {"'", "-"}
    punct_to_remove = ''.join(ch for ch in string.punctuation if ch not in keep)
    s = re.sub(f"[{re.escape(punct_to_remove)}]", "", s)
    s = re.sub(r"\s+", " ", s)
    s = s.strip()   
    return s


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    # run_tests()
    pass