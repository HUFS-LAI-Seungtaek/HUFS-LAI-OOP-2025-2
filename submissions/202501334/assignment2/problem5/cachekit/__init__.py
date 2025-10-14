VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._store = {}

    def put(self, key, value) -> None:
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)

    def __len__(self) -> int:
        return len(self._store)

    def clear(self) -> None:
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]