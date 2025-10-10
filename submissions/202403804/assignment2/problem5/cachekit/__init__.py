from typing import Any, Optional
VERSION = "1.0" # VERSION: str (예: "1.0")

def print_version_info() -> None: #(간단 출력)
    print(f"CacheKit version {VERSION}")

class Cache:
    def __init__(self) -> None: # 내부 dict 초기화
        self.cache = {}
    def put(self, key, value) -> None:
        self.cache[key] = value
    def get(self, key, default=None) -> Optional[Any]:
        return self.cache.get(key, default)
    def __len__(self) -> int:
        return len(self.cache)
    def clear(self) -> None:
        self.cache.clear()
__all__ = ["Cache", "print_version_info", "VERSION"]