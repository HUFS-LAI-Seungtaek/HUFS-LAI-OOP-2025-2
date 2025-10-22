# VERSION
VERSION = "1.0"

# 버전 정보 출력
def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

# Cache 클래스
class Cache:
    def __init__(self) -> None:
        self._data = {}

    def put(self, key, value) -> None:
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __len__(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()

# 루트에서 노출할 API
__all__ = ["Cache", "print_version_info", "VERSION"]
