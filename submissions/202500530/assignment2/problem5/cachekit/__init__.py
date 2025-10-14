VERSION = "3.0"

def print_version_info() -> None: #(간단 출력)
    print(f"{VERSION}")

#gpt
# dict의 method에 무엇이 있는지 물어보고 그에 대한 개념을 물어보았습니다.
# 함수의 변수를 줄이는 과정과 @의 오용을 없애는 과정에서 gpt의 도움을 받았습니다.

class Cache:
    def __init__(self) -> None: #내부 dict 초기화
        self._dict = {}
    
    def put(self, key, value) -> None:
        self._dict[key] = value

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def __len__(self) -> int:
        return len(self._dict)

    def clear(self) -> None:
        self._dict.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
