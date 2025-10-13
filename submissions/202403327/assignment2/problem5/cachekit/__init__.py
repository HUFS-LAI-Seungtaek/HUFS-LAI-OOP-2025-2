VERSION = "1.0"
def print_version_info():
    """Prints the version of the cachekit package."""
    print(f"cachekit version {VERSION}")
class Cache:
    def __init__(self):
        self._storage = {}

    def put(self, key, value):
        self._storage[key] = value

    def get(self, key, default=None):
        return self._storage.get(key, default)

    def __len__(self):
        return len(self._storage)

    def clear(self):
        self._storage = {}
__all__ = ["Cache", "print_version_info", "VERSION"]