"""
cachekit: a tiny in-memory cache wrapper
Public API:
- VERSION: str
- print_version_info(): None
- Cache: dict-backed cache with put/get/len/clear
"""

from typing import Any, Dict

VERSION: str = "1.0"

def print_version_info() -> None:
    print(f"cachekit {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._store: Dict[Any, Any] = {}

    def put(self, key: Any, value: Any) -> None:
        self._store[key] = value

    def get(self, key: Any, default: Any = None) -> Any:
        return self._store.get(key, default)

    def __len__(self) -> int:
        return len(self._store)

    def clear(self) -> None:
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
