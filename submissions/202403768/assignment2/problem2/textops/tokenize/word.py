def word_tokens(s: str) -> list[str]:
    """
    Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """

    if not s or s.strip() == "":
       return []
    else:
       return s.split(" ")
   
"""
위에 def 설명이 직관적으로 이해가 안돼서 파파고 돌려봤습니다.
"""

if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    run_tests()
    pass