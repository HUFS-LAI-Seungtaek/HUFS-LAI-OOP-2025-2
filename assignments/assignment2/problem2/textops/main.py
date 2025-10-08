if __name__ == "__main__":
    try:
        from . import clean_text, word_tokens
        s = "  Hello,   WORLD!  "
        cleaned = clean_text(s)
        print(cleaned)
        print(word_tokens(cleaned))
        print("textops demo OK")
    except Exception as e:
        print("Implement textops first:", e)
