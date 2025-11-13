import re
import string

def clean_text(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    s = re.sub(r"\s+", " ", s.lower().strip())
    keep = {"'", "-"}
    table = {ord(ch): None for ch in string.punctuation if ch not in keep}
    s = s.translate(table)
    s = re.sub(r"\s+", " ", s).strip()
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
