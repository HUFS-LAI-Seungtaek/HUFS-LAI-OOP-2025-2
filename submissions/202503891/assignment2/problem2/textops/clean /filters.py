import re

def clean_text(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r"[!\"#$%&()*+,./:;<=>?@[\\]^_`{|}~]", "", s)
    return s
'''string.punctuation을 사용해 보았습니다.
import re
import string

def clean_text(s: str) -> str:
    s = s.lower().strip()                     # 1. 소문자 변환 및 양쪽 공백 제거
    s = re.sub(r'\s+', ' ', s)                # 2. 여러 공백을 하나로
    s = re.sub(f"[{re.escape(string.punctuation)}]", "", s)  # 3. 모든 문장부호 제거
    return s

'''
