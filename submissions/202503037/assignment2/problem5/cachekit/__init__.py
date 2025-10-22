class Cache:
    def __init__(self):
        self._data = {}
    def put(self, key, value):
        self._data[key] = value
    def get(self, key, default=None):
        return self._data.get(key, default)
    def __len__(self):
        return len(self._data)
    def clear(self):
        self._data.clear()

VERSION: str = "0.1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

__all__ = ["Cache", "print_version_info", "VERSION"]
