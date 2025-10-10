from . import Cache, print_version_info

if __name__ == "__main__":
    def run_demo():
        # Instructor's quick test from README
        print_version_info()
        c = Cache()
        c.put("a", 1)
        print("Length:", len(c), "Value:", c.get("a"))
        c.put("a", 999)
        print("Updated Value:", c.get("a"))
        c.clear()
        print("Length after clear:", len(c))
        print("Missing key with default:", c.get("missing", 42))

    run_demo()