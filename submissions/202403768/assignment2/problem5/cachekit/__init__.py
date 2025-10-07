VERSION = "1.0"

def print_version_info() -> None:
    return f'Cache version: {VERSION}'

class Cache:
    def __init__(self) -> None:
        self._data = {}
# __init__ 매개변수가 self 만 있을 때 어떻게 해야하는 지 제미나이한테 물어봤습니다.
    
    def put(self, key, value) -> None:
        self._data[key] = value
#딕셔너리 값 추가 참고: https://devinside.tistory.com/161

    def get(self, key, default=None):
        return self._data.get(key, default)
# .get() 함수: https://velog.io/@ash5541/get-get%EB%A9%94%EC%84%9C%EB%93%9C%EB%9E%80

    def __len__(self) -> int:
        return len(self._data)
    
    def clear(self) -> None:
        self._data = {}
    
__all__ = ["Cache", "print_version_info", "VERSION"]
        
