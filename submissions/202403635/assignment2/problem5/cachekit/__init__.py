# 생성형 AI Gemini 사용범위: 코드 초안 생성, 파이썬 특정 기능과 코드 제안 및 설명 (코드 제안 시 같은 줄에 명시), 작성한 코드 리뷰 요청

"""루트 제공:

VERSION: str (예: "1.0")
print_version_info() -> None (간단 출력)
class Cache:
__init__(self) -> None — 내부 dict 초기화
put(self, key, value) -> None
get(self, key, default=None)
__len__(self) -> int
clear(self) -> None
__all__ = ["Cache", "print_version_info", "VERSION"]
"""

# VERSION: str (예: "1.0")
VERSION = "1.0"
# print_version_info() -> None (간단 출력)
def print_version_info() -> None:
    print(f"버전은 {VERSION}입니다.")

class Cache:
    def __init__(self) -> None:
        self._data = {}

    def put(self, key, value) -> None:
        self._data[key] = value 

    def get(self, key, default=None):
        return self._data.get(key, default) # 해당 코드를 생성형 AI Gemini를 통해 제안받고 상세한 설명을 요청했습니다.

    def __len__(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]
