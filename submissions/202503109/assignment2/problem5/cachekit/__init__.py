# cachekit/__init__.py

# Public version string
VERSION: str = "1.0"

def print_version_info() -> None:
    """Print a short version banner."""
    print(f"cachekit {VERSION}")

class Cache:
    """A tiny in-memory cache wrapping a dict."""

    def __init__(self) -> None:
        # Internal storage; do not print in library code for testability
        self._store: dict = {}

    def put(self, key, value) -> None:
        """Insert or overwrite a value by key."""
        self._store[key] = value

    def get(self, key, default=None):
        """Return the value for key if present; otherwise default."""
        return self._store.get(key, default)

    def __len__(self) -> int:
        """Number of items in the cache."""
        return len(self._store)

    def clear(self) -> None:
        """Remove all items."""
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]

# 캐시구조를 배우기위해 AI 주석 남겨둠
