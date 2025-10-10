# Demo for textops package
if __name__ == "__main__":
    try:
        from textops import clean_text, word_tokens
        s = "  Hello,   WORLD!  "
        cleaned = clean_text(s)
        print(cleaned)                  # expected: "hello world"
        print(word_tokens(cleaned))     # expected: ["hello", "world"]
        print("textops demo OK")
    except Exception as e:
        print("Implement textops first:", e)
"""
(도움받은 내용):
textops 패키지를 구현하는 과정에서 생성형 AI(Gemini)의 도움을 받아, 파이썬 패키지의 전체적인 구조, __init__.py의 역할, 상대 경로 임포트의 원리를 학습했습니다. 또한 clean_text 함수의 문자열 불변성 개념과 re.sub 사용법, ModuleNotFoundError 디버깅 과정에서 도움을 받았습니다.
"""