import re
import string

def clean_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    keep = {"'", "-"}
    punc = set(string.punctuation) - keep
    s = s.translate(str.maketrans("","", "".join(punc))) # gpt 도움을 받음 
    # .join -> set을 다시 문자열, maketrans(바뀔문자,바꿀문자,삭제할문자)
    return s


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    #run_tests()
    #pass