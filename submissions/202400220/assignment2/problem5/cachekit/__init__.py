# perplexity의 도움을 많이 받은 부분. 전반적인 개념 이해와 구현에 도움을 받았다.
# 캐시는 무엇인지, 각각의 함수는 무엇을 어떻게 수행해야 하는지 등을 이해할 수 있었다.

VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

class Cache:
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

__all__ = ["Cache", "print_version_info", "VERSION"]