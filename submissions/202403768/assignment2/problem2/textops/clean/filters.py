import re
import string

punc_to_remove = set(string.punctuation) - {"'", "-"}

def clean_text(s:str) -> str:
  s = s.lower()
  s = re.sub(r'\s+', ' ', s)
  s = s.strip()
  s = "".join(char for char in s if char not in punc_to_remove)

  return s

if __name__ == "__main__":
  def run_tests():
    assert clean_text(" Hello, WORLD! ") == "hello world"
    assert clean_text("\tROCK-'N'-ROLL!!") == "rock-'n'-roll"
    assert clean_text("...") == ""
    assert clean_text(" A B\tC\nD") == "a b c d"
    print("filters.py tests passed.")
  run_tests()
  pass