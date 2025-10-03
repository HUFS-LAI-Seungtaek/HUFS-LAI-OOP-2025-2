from . import clean_text, word_tokens

if __name__ == "__main__":
    s = "  Hello,   WORLD!  "
    print(clean_text(s))
    print(word_tokens(clean_text(s)))
