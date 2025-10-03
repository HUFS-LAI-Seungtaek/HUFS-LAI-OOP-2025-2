# cachekit/__init__.py

VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version: {VERSION}")

class Cache:
    """
    A simple in-memory key-value cache.
    """
    def __init__(self) -> None:
        self._data = {}

    def put(self, key, value) -> None:
        """Stores a value for the given key."""
        self._data[key] = value

    def get(self, key, default=None):
        """Retrieves a value for the given key, or a default if not found."""
        return self._data.get(key, default)

    def __len__(self) -> int:
        """Returns the number of items in the cache."""
        return len(self._data)

    def clear(self) -> None:
        """Removes all items from the cache."""
        self._data.clear()

__all__ = ["VERSION", "print_version_info", "Cache"]
