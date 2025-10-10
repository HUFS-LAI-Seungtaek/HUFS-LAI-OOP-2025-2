def word_tokens(s: str) -> list[str]:
    if not s or s.strip() == "":
        return []
    tokens = s.split(" ")
    return [token for token in tokens if token.strip()] # gpt 도움을 받음 
    #원래는 빈 문자열을 만들고 append를 이용함 

if __name__ == "__main__":
    def run_tests():
        assert word_tokens("hello world") == ["hello", "world"]
        assert word_tokens("") == []
        assert word_tokens(" ") == []
        assert word_tokens("single") == ["single"]
        print("word.py tests passed.")
    #run_tests()
    #pass