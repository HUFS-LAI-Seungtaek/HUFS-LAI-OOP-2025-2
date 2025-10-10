# Demo for textops package
if __name__ == "__main__":
    try:
        import clean.filters, tokenize.word
        s = "  Hello,   WORLD!  "
        cleaned = clean.filters.clean_text(s)
        print(cleaned)                  # expected: "hello world"
        print(tokenize.word.word_tokens(cleaned))     # expected: ["hello", "world"]
        print("textops demo OK")
    except Exception as e:
        print("Implement textops first:", e)