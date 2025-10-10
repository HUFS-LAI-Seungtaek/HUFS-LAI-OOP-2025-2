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
    
    # 1. 소문자로 변환
    s = s.lower()
    
    # 2. apostrophes와 hyphens를 제외한 문장부호 제거
    keep = {"'", "-"}
    to_remove = set(string.punctuation) - keep
    translator = str.maketrans('', '', ''.join(to_remove))
    s = s.translate(translator)

    # 3. 모든 연속 공백을 단일 공백으로 압축
    s = re.sub(r"\s+", " ", s)

    # 4. 앞뒤 공백 제거
    s = s.strip()

    return s


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()