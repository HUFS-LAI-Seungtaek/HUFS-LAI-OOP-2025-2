VERSION = "1.0"

def print_version_info() -> None:
    print(VERSION)

class Cache:
    def __init__(self) -> None:
        self._dict = {}

    def put(self, key, value) -> None:
        self._dict[key] = value

    def get(self, key, default = None):
        return self._dict.get(key, default)
    
    def __len__(self) -> int:
        return len(self._dict)
    
    def clear(self) -> None:
        self._dict.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]