# cachekit/main.py
if __name__ == "__main__":
    from . import Cache, print_version_info

    print_version_info()

    c = Cache()
    c.put("a", 1)
    print("Length:", len(c), "Value for 'a':", c.get("a"))  # 1 1

    c.put("a", 999)
    print("Updated 'a':", c.get("a"))                        # 999

    c.clear()
    print("Length after clear:", len(c))                     # 0

    print("Missing key with default:", c.get("missing", 42)) # 42
 #메인 함수+이니셜 함수 구현에 gpt도움 받았습니다.