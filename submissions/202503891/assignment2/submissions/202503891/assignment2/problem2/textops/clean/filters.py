import re
import string

def clean_text(s: str) -> str:
    """
    Pipeline:
      1) lowercase
      2) strip
      3) collapse all whitespace to single spaces
      4) remove ASCII punctuation except apostrophes (') and hyphens (-)
    """
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    s = s.strip()

    keep = {"'", "-"}
    remove = set(string.punctuation) - keep

    s = ''.join(ch for ch in s if ch not in remove)

    return s
