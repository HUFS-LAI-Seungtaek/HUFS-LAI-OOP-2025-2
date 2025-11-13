"""
cachekit: simple memory cache; root re-export
"""

VERSION = "1.0"

def print_version_info() -> None:
    """cachekit 패키지의 버전 정보를 출력합니다."""
    print(f"cachekit version {VERSION}")

class Cache:
    """
    내부적으로 딕셔너리를 사용하는 간단한 인-메모리 캐시 클래스입니다.
    """
    def __init__(self) -> None:
        self._cache: dict = {}

    def put(self, key, value) -> None:
        """키-값 쌍을 캐시에 저장합니다. 동일한 키가 있으면 덮어씁니다."""
        self._cache[key] = value

    def get(self, key, default=None):
        """키를 사용해 값을 가져옵니다. 키가 없으면 default 값을 반환합니다."""
        return self._cache.get(key, default)

    def __len__(self) -> int:
        return len(self._cache)

    def clear(self) -> None:
        """캐시의 모든 항목을 삭제합니다."""
        self._cache.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]