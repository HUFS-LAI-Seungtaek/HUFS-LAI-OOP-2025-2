"""
cachekit: 간단한 메모리 캐시 패키지

파이프라인 중간 결과를 임시 저장하기 위한 경량 캐시 시스템
"""

# 패키지 버전 정보
VERSION = "1.0"


def print_version_info() -> None:
    """패키지 버전 정보를 출력합니다."""
    print(f"cachekit v{VERSION} - Simple Memory Cache Package")


class Cache:
    """
    딕셔너리 기반의 간단한 메모리 캐시 클래스
    
    파이프라인에서 중간 결과나 계산된 값들을 임시로 저장하고
    빠르게 접근할 수 있도록 도와주는 캐시 시스템입니다.
    """
    
    def __init__(self) -> None:
        """캐시 인스턴스를 초기화합니다."""
        # 내부 저장소로 딕셔너리 사용
        self._storage = {}
    
    def put(self, key, value) -> None:
        """
        캐시에 키-값 쌍을 저장합니다.
        
        Args:
            key: 저장할 키 (모든 해시 가능한 타입)
            value: 저장할 값 (모든 타입)
        """
        self._storage[key] = value
    
    def get(self, key, default=None):
        """
        캐시에서 키에 해당하는 값을 조회합니다.
        
        Args:
            key: 조회할 키
            default: 키가 존재하지 않을 때 반환할 기본값
            
        Returns:
            키에 해당하는 값 또는 기본값
        """
        return self._storage.get(key, default)
    
    def __len__(self) -> int:
        """
        캐시에 저장된 항목의 개수를 반환합니다.
        
        Returns:
            저장된 키-값 쌍의 개수
        """
        return len(self._storage)
    
    def clear(self) -> None:
        """캐시의 모든 데이터를 삭제합니다."""
        self._storage.clear()
    
    def __repr__(self) -> str:
        """캐시 객체의 문자열 표현을 반환합니다."""
        return f"Cache(items={len(self._storage)})"


# 공개 API 정의
__all__ = ["Cache", "print_version_info", "VERSION"]