import re
import string

def clean_text(s: str) -> str:
   s = s.lower() 
   s = re.sub(r"\s+", " ", s) 
   s = s.strip() 
   keep = {"'", "-"} #유지할 문자 set으로 정의
   remove = set(string.punctuation) - keep  
   # string.punctuation : 표준 문장부호 포함 문자열  -> set으로 변환 
   # => 제거할 문자열들만을 포함하는 remove set 생성
   punctuation_pattern = "[" + re.escape("".join(remove)) + "]"
   # "".join() : remove내의 요소들을 연결 
   # re.escape() : 다른 의미를 가진 문자들을 다른 문자들과 같이 평범한 문자로 취급
   # punctuation_pattern = [제거할 문자열]
   s = re.sub(punctuation_pattern, "", s)
   s = re.sub(r"\s+", " ", s)
   s = s.strip()
   return s


if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
pass