# main.py
"""
Demo for textops package.
"""

if __name__ == "__main__":
    try:
        # Relative import, as this script is part of the 'textops' package
        from . import clean_text, word_tokens
        
        s = "  Hello,   WORLD!  "
        
        cleaned = clean_text(s)
        print(cleaned)               # expected: "hello world"
        
        tokens = word_tokens(cleaned)
        print(tokens)   # expected: ["hello", "world"]
        
        print("textops demo OK")

    except ImportError:
        print("Failed to import textops components.")
        print("Please run this file as a module from the project's root directory.")
        print("Example: python -m textops.main")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")