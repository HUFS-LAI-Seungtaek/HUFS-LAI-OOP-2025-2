# Demo for textops package
from textops import clean_text, word_tokens
if __name__ == "__main__":
    try:
        s = "  Hello,   WORLD!  "
        cleaned = clean_text(s)
        print(cleaned)                  # expected: "hello world"
        print(word_tokens(cleaned))     # expected: ["hello", "world"]
        print("textops demo OK")
    except Exception as e:
        print("Implement textops first:", e) #야호 성공!!