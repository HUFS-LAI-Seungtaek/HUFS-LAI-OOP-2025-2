from textops import clean_text, word_tokens

def main():
    print("--- Демонстрация пакета textops ---")
    
    tests = [
        "  Hello,   WORLD!  ",           
        " \tHello,\nWORLD!!!  ", 
        "...",                            
        "ROCK-'N'-ROLL!!",               
        "",                             
        " ",                              
        "  a\t\nb "
    ]
    
    expected_clean = [
        "hello world",
        "hello world",
        "",
        "rock-'n'-roll",
        "",
        "",
        "a b"
    ]
    
    expected_tokens = [
        ['hello', 'world'],
        ['hello', 'world'],
        [],
        ['rock-\'n\'-roll'],
        [],
        [],
        ['a', 'b']
    ]

    for i, s in enumerate(tests):
        try:
            cleaned = clean_text(s)
            tokens = word_tokens(cleaned)
            
            print(f"Тест {i+1}:")
            print(f"  Оригинал:   '{s}'")
            print(f"  Очищено:    '{cleaned}' (Ожидается: '{expected_clean[i]}')")
            print(f"  Токены:     {tokens} (Ожидается: {expected_tokens[i]})")
            print("-" * 20)
        except Exception as e:
            print(f"Ошибка при обработке '{s}': {e}")
            print("-" * 20)


if __name__ == "__main__":
    main()
