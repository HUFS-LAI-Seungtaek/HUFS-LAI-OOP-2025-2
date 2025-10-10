# cachekit/__init__.py

VERSION = "1.0"

def print_version_info() -> None:
    """간단한 버전 정보 출력 함수 (데모용)"""
    print(f"cachekit version: {VERSION}")

class Cache:
    """
    내부 dict를 사용하는 단순 메모리 캐시 클래스.
    """
    def __init__(self) -> None:
        """내부 dict를 초기화합니다."""
        self._data = {}

    def put(self, key, value) -> None:
        """키-값을 캐시에 저장합니다."""
        self._data[key] = value

    def get(self, key, default=None):
        """키에 해당하는 값을 반환합니다. 키가 없으면 default 값을 반환합니다."""
        return self._data.get(key, default)

    def clear(self) -> None:
        """캐시 내용을 모두 지웁니다."""
        self._data.clear()

    def __len__(self) -> int:
        """캐시에 저장된 항목의 개수를 반환합니다."""
        return len(self._data)

# 외부로 노출할 API 목록 정의
__all__ = ["Cache", "print_version_info", "VERSION"]
