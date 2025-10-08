import re
import string

def clean_text(s: str) -> str:

    s = s.lower()

    s = s.strip()

    s = re.sub(r"\s+", " ", s)

    keep = {"'", "-"}
    remove = set(string.punctuation) - keep
    s = "".join(ch for ch in s if ch not in remove)

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
