import re
import string

def clean_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    keep = {"'", "-"}
    remove = set(string.punctuation) - keep
    translator = str.maketrans('', '', str(remove))
    s = s.translate(translator)
    return s
# string 관련 2주차 강의pdf 참고하였습니다.
#translator 사용은 ChatGPT 활용하여 사용법 이해 후 작성하였습니다.

if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
