if __name__ == "__main__":
    from . import Cache, print_version_info, VERSION

    def run_tests():
        print_version_info()
        c = Cache()
        c.put("a", 1)
        c.put("b", "test_val")
        assert len(c) == 2
        assert c.get("a") == 1
        assert c.get("b") == "test_val"
        c.put("a", 999)
        assert len(c) == 2 
        assert c.get("a") == 999
        assert c.get("missing", 42) == 42
        assert c.get("not_there") is None 
        c.clear()
        assert len(c) == 0
        assert isinstance(VERSION, str)
        assert len(VERSION) > 0
    run_tests()
    pass 