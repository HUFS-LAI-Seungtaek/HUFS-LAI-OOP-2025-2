"""
cachekit: A simple in-memory cache utility.
"""

# 1. 패키지 버전 정보
VERSION = "1.0"

# 2. 버전 정보를 출력하는 함수
def print_version_info():
    """
    cachekit 패키지의 이름과 버전 정보를 출력합니다.
    """
    print(f"cachekit version {VERSION}")

# 3. Cache 클래스 구현
class Cache:
    """
    간단한 메모리 내 키-값 캐시를 제공하는 클래스.
    내부적으로 파이썬 딕셔너리를 사용합니다.
    """
    def __init__(self) -> None:
        """
        Cache 인스턴스를 초기화합니다.
        내부에 빈 딕셔너리를 생성하여 데이터를 저장합니다.
        """
        # 외부에서 직접 접근하지 않도록 _(언더스코어)로 시작하는 변수명을 사용합니다.
        self._cache = {}

    def put(self, key, value) -> None:
        """
        캐시에 키-값 쌍을 저장하거나 덮어씁니다.

        Args:
            key: 저장할 데이터의 키.
            value: 저장할 데이터의 값.
        """
        self._cache[key] = value

    def get(self, key, default=None):
        """
        키를 사용해 캐시에서 값을 조회합니다. 키가 없으면 default 값을 반환합니다.

        Args:
            key: 조회할 데이터의 키.
            default (optional): 키가 없을 때 반환할 기본값. Defaults to None.

        Returns:
            조회된 값 또는 기본값.
        """
        return self._cache.get(key, default)

    def __len__(self) -> int:
        """
        캐시에 저장된 아이템의 개수를 반환합니다. (len(cache_instance) 형태로 사용 가능)
        """
        return len(self._cache)

    def clear(self) -> None:
        """
        캐시의 모든 아이템을 삭제합니다.
        """
        self._cache.clear()

# 4. `from cachekit import *` 사용 시 공개할 API 목록 정의
__all__ = [
    "Cache",
    "print_version_info",
    "VERSION"
]
