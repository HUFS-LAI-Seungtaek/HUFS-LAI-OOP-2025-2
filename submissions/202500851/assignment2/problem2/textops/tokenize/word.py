def word_tokens(s: str) -> list[str]:
    if not s == "" or s.strip() == "":
        return []
    else:
        return s.split(" ")
#2주차 강의pdf에서 if 관련 문법 참고하였습니다.

if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    run_tests()
