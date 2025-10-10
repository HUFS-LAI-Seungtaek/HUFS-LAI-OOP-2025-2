if __name__ == "__main__":
    try:
        from . import clean_text, word_tokens
        s = "  Hello,   WORLD!  "
        c = clean_text(s)
        print(c)
        print(word_tokens(c))
        print("textops demo OK")
    except Exception as e:
        print("Implement textops first:", e)