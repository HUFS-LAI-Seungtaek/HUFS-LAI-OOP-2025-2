from . import clean_text, word_tokens

def demo():
    s = "  Hello,   WORLD!  "
    cleaned = clean_text(s)
    tokens = word_tokens(cleaned)
    print(cleaned)               # expected: "hello world"
    print(tokens)                # expected: ["hello", "world"]
    print("textops demo OK")

if __name__ == "__main__":
    try:
        demo()
    except Exception as e:
        print("Implement textops first:", e)
