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
    keep = {"'", "-"}
    remove_str = set(string.punctuation) - keep
    s = "".join(ch for ch in s if ch not in remove_str) #윗줄까지 쓰고 실행이 안되어 지피티에게 물어본 문장
    # == for ch in s: if ch not in remove_str: 문자열에 추가 -> 그걸 가지고 문장다시 구성(=.join)
    return s



    # TODO: 구현하세요
    # 힌트:
    # 1) s.lower() - 소문자 변환
    # 2) re.sub(r"\s+", " ", s) - 모든 연속 공백을 단일 공백으로
    # 3) s.strip() - 앞뒤 공백 제거
    # 4) string.punctuation에서 특정 문자 제외하고 제거
    # 5) set 연산을 활용해서 keep = {"'", "-"}, 나머지는 제거

if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
    pass
