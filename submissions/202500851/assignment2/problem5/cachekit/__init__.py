#ChatGPT를 통해서 문제 이해한뒤 코드 작성했습니다.

VERSION: str = 1.0

def print_version_info() -> None:
    print(f"VERSION : {VERSION}")
#2주차 강의pdf에서 print 사용법 참고하였습니다.

class Cache :
    def __init__(self) -> None:
        self._storage = {}

    def put(self, key, value) -> None:
        self._storage[key] = value
        
    def get(self, key, default=None):
        return self._storage.get(key, default)

    def __len__(self) -> int:
        return len(self._storage)

    def clear(self) -> None:
        self._storage.clear()
#ChatGPT로 dictionary 사용법 더 자세하게 배운 뒤 사용하였습니다.

__all__ = ["Cache", "print_version_info", "VERSION"]