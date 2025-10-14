# TODO: 구현하세요
# 힌트:
# 1) 빈 문자열이나 공백만 있는 경우 체크: if not s or s.strip() == ""
# 2) 단일 공백으로 분할: s.split(" ")
# 3) 빈 리스트 반환 조건 잊지 말기
# - 규칙:
# - 단일 공백 기준 분할
# - 빈 문자열/공백뿐이면 [] 반환
def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume s is already normalized by clean_text.
    """

    if not s or s.strip() == "":
        return []

    s = s.split(" ")
    s = [t for t in s if t != ""]

    return s


if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        assert word_tokens("hi  there") == ["hi", "there"]
        print("word.py tests passed.")

    run_tests()
    pass
