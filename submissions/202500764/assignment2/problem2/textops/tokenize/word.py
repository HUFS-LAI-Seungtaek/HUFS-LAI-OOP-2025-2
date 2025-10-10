def word_tokens(s: str) -> list[str]:
 
  """
  Split on single spaces; empty/whitespace-only -> [].
    Assume `s` is already normalized by clean_text.
    """
  if not isinstance(s, str):
        raise TypeError("word_tokens: 입력은 문자열이어야 합니다.")

        s = s.strip()
        if not s:
         return []
    
        return s.split(" ")


if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    # run_tests()
    pass