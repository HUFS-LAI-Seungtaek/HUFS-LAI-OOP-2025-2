VERSION = "1.0"

def print_version_info():
    print(f"cachekit {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._store = {}

    def put(self, key, value) -> None:
       self._store[key] = value 

    def get(self, key, default=None):
        return self._store.get(key, default) #gpt 도움을 받음 
        #if문을 활용해 존재하지 않는 키를 구별하려고 했으나, get 용법을 이용. 
        #get에서 ',' 앞은 확인 대상, ','뒤는 없을 때 대신 줄 값

    def __len__(self) -> int:
        return len(self._store)

    def clear(self) -> None:
       self._store.clear() #gpt 도움을 받음 
       #파이썬 내장 메서드로, 딕셔너리 안의 모든 항목을 지움

__all__ = ["Cache", "print_version_info", "VERSION"]