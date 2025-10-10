# Demo for textops package
if __name__ == "__main__":
    from textops import clean_text, word_tokens

    s = " \tHello,\nWORLD!!!  "
    cleaned = clean_text(s)           # "hello world"
    tokens = word_tokens(cleaned)     # ["hello", "world"]

    print(cleaned)
    print(tokens)
