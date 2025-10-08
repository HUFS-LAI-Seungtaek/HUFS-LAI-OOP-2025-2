import re
import string

def clean_text(s: str) -> str:
    """
    규칙:
    - 전부 소문자
    - 앞뒤 공백 제거
    - 모든 연속 공백(스페이스/탭/개행 등) 한 칸으로 축약
    - ASCII 문장부호 제거 (단, apostrophe ' 과 hyphen - 는 유지)
    """
    if not isinstance(s, str):
        raise TypeError("clean_text: input must be str")

    # 1) 소문자화
    s = s.lower()

    # 2) ASCII punctuation 중 '와 -만 남기고 나머지 제거
    # string.punctuation: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
    punct_to_remove = string.punctuation.replace("'", "").replace("-", "")
    s = s.translate(str.maketrans("", "", punct_to_remove))

    # 3) 모든 공백 축약 + 트림
    s = re.sub(r"\s+", " ", s).strip()

    return s
