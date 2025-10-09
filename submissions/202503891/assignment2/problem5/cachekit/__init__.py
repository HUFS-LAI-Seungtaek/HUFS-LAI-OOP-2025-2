VERSION = "1.0"

def print_version_info():
    print(f"CacheKit version {VERSION}")

class Cache:
    def __init__(self):
        self._store = {}

    def put(self, key, value):
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)

    def __len__(self):
        return len(self._store)

    def clear(self):
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]

'''credit:Cache 클래스를 구현할 때, 내부 dict를 래핑하여 put/get/clear/__len__의 기능을 
설계하는 방법을 gpt를 참고하였습니다.
'''
