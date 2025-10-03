def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """
    # TODO: 구현하세요
    # 힌트:
    if not s or s.strip() == "":
        return []

    return s.split(" ")
    # 3) 빈 리스트 반환 조건 잊지 말기
    


if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    # run_tests()
    pass