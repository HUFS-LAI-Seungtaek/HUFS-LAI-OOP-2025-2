'''## Required API
루트 제공:
- `VERSION: str` (예: "1.0")
- `print_version_info() -> None` (간단 출력)
- `class Cache`:
  - `__init__(self) -> None` — 내부 dict 초기화
  - `put(self, key, value) -> None`
  - `get(self, key, default=None)`
  - `__len__(self) -> int`
  - `clear(self) -> None`
- `__all__ = ["Cache", "print_version_info", "VERSION"]`
'''

VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version: {VERSION}")


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