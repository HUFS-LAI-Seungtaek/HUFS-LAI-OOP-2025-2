VERSION = "1.0"

def print_version_info():
    print(f"cachekit 버전: {VERSION}")

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

__all__ = ["Cache", "print_version_info", "VERSION"]