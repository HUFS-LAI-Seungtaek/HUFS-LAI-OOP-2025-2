def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """
    # 1. 빈 문자열이나 공백만 있는 경우 체크 및 빈 리스트 반환
    if not s or s.strip() == "":
        return []

    # 2. 단일 공백으로 분할
    # s는 이미 clean_text에 의해 정규화되었으므로, 불필요한 공백은 제거되거나 축약되어 있습니다.
    return s.split(" ")


if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []  # 공백만 있는 경우 처리
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    run_tests()