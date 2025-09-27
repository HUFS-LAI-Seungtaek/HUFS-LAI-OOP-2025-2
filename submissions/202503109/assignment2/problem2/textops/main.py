# Demo for textops package

        
from textops import clean_text, word_tokens
s = "  Hello,   WORLD!  "
cleaned = clean_text(s)
print(cleaned)                  # expected: "hello world"
print(word_tokens(cleaned))     # expected: ["hello", "world"]
print("textops demo OK")