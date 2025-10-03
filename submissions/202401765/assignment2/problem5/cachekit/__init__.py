VERSION = "1.0"

def print_version_info() -> None:
    print(f"Cachekit Version: {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._cache = {}

    def put(self, key, value) -> None:
        self._cache[key] = value

    def get(self, key, default=None):
        return self._cache.get(key, default)

    def __len__(self) -> int:
        return len(self._cache)

    def clear(self) -> None:
        self._cache.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]