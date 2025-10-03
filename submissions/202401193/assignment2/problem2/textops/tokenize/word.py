def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """
    if s and s.strip():
        li = s.split(" ")
    else:
        li = []
    return li

# 이 파트 제미나이의 도움을 받았습니다

if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    
    run_tests()
