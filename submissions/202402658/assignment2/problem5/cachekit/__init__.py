VERSION = "1.0.0"

def print_version_info() -> None :
    print(VERSION)

class Cache:
    def __init__(self) -> None :
        self._d = {}

    def put(self, key, value) -> None :
        self._d[key] = value

    def get(self, key, default=None) :
        return self._d.get(key, default)

    def __len__(self) -> int : 
        return len(self._d)

    def clear(self) -> None :
        self._d.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
