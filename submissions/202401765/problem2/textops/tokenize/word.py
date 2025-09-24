def word_tokens(s: str) -> list[str]:
    """
    Split a string into a list of words based on single spaces.
    Returns an empty list for empty or whitespace-only strings.
    """
    if not s.strip():
        return []
    
    return s.split(' ')

if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("hello") == ["hello"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("   ") == []
        print("word.py tests passed.")
    run_tests()