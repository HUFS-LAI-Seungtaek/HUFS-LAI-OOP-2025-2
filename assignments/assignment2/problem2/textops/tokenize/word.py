def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """
    # TODO: 구현하세요
    raise NotImplementedError


if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    # run_tests()
    pass