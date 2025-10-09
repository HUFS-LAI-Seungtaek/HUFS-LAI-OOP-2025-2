# 패키지 버전
VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._store = {}

    def put(self, key, value) -> None:
        """캐시에 key-value 저장 (덮어쓰기 허용)"""
        self._store[key] = value

    def get(self, key, default=None):
        """캐시에서 key 조회. 없으면 default 반환."""
        return self._store.get(key, default)

    def __len__(self) -> int:
        """캐시 내 데이터 개수 반환"""
        return len(self._store)

    def clear(self) -> None:
        """캐시 초기화"""
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
