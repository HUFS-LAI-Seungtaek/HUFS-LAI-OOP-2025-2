#demo

if __name__ == "__main__":
    from . import Cache, print_version_info , VERSION
    print_version_info()
    c = Cache(); c.put("a", 1)
    print(len(c), c.get("a"))   # 1 1
    c.clear(); print(len(c))    # 0
