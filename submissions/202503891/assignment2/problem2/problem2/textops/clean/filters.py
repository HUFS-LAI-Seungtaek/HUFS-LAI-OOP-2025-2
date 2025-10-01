import re

def clean_text(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r"[!\"#$%&()*+,./:;<=>?@[\\]^_`{|}~]", "", s)
    return s
