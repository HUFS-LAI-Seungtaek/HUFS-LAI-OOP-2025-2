VERSION: str = "1.0"
def print_version_info() -> None:
    print (f"Cachekit Version: {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._data = {}
    def put(self, key, value) -> None:
        self._data[key] = value
    def get(self, key, default = None):
        return self._data.get(key, default)
    def __len__(self) -> int:
        return len(self._data)
    def clear(self) -> None:
        self._data.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
