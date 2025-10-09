if __name__ == "__main__":
    from . import Cache, print_version_info

    print_version_info()  # 버전 정보 출력

    c = Cache()
    c.put("a", 1)
    print(len(c), c.get("a"))   # 1 1

    c.put("a", 999)
    print(c.get("a"))           # 999

    c.clear()
    print(len(c))               # 0

    print(c.get("missing", 42)) # 42
