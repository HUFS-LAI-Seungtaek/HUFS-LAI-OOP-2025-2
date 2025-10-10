# cachekit/__init__.py

# 1. VERSION 정의
VERSION: str = "1.0"

# 2. print_version_info 함수 정의
def print_version_info() -> None:
    """
    현재 패키지의 버전을 간단히 출력합니다.
    """
    # 라이브러리 내부이지만, 요구사항에 따라 print를 사용합니다.
    print(f"cachekit version: {VERSION}")

# 3. Cache 클래스 정의
class Cache:
    """
    아주 단순한 메모리 캐시 클래스. 내부적으로 dict를 사용하여 데이터를 저장합니다.
    """
    
    def __init__(self) -> None:
        """
        내부 캐시 저장소(딕셔너리)를 초기화합니다.
        """
        self._store = {}

    def put(self, key, value) -> None:
        """
        키-값 쌍을 캐시에 저장합니다.
        """
        # 동일 키 덮어쓰기는 dict의 기본 동작으로 허용됩니다.
        self._store[key] = value

    def get(self, key, default=None):
        """
        키에 해당하는 값을 가져옵니다. 키가 없으면 default 값을 반환합니다.
        """
        # dict의 .get() 메서드를 활용하여 Edge Case를 간단히 처리합니다.
        return self._store.get(key, default)

    def clear(self) -> None:
        """
        캐시의 모든 항목을 제거합니다.
        """
        self._store.clear()
        
    # 특수 메서드: len(cache)를 가능하게 합니다.
    def __len__(self) -> int:
        """
        캐시에 저장된 항목의 개수를 반환합니다.
        """
        return len(self._store)

# 4. 공개 API 정의
__all__ = ["Cache", "print_version_info", "VERSION"]