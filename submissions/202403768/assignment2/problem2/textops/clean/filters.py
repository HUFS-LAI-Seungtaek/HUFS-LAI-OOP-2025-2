import re
import string

keep = {"'", "-"}
punc = set(string.punctuation) - keep

def clean_text(s: str) -> str:

    s = s.lower()
    s = re.sub(r'\s+', ' ', s)
    s = s.strip()

    need = []
    for char in s:
      if char not in punc:
        need.append(char)
      s = "".join(need)
    return s

'''
.join() 함수에는 리스트가 들어가야 된다고 해서 
리스트 need 라는 빈 리스트를 만들어 반복문으로 불필요한 문자를 제거하고 .join으로 모았습니다.
# .join() 함수에 대해서는 https://blockdmask.tistory.com/468 를 참조했습니다.
# 반복문으로 리스트를 만드는 방법은 https://2030bigdata.tistory.com/109 를 참조했습니다.

처음 need를 전역변수로 만들었다가 작동이 제대로 안되어서 
제미나이에게 왜 안되는건지 물어봐서 지역변수로 수정했습니다.
'''

if __name__ == "__main__":
    def run_tests():
        assert clean_text("  Hello,   WORLD!  ") == "hello world"
        assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
        assert clean_text("...") == ""
        assert clean_text(" A  B\tC\nD ") == "a b c d"
        print("filters.py tests passed.")
    run_tests()
    pass
