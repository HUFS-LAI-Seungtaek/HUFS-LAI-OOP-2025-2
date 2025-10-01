VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self) -> None:
        self._store: dict = {}

    def put(self, key, value) -> None:
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)

    def __len__(self) -> int:
        return len(self._store)

    def clear(self) -> None:
        self._store.clear()


if __name__ == "__main__":
    print_version_info()
    c = Cache()
    c.put("a", 1)
    print(len(c), c.get("a"))   # 1 1
    c.put("a", 999)
    print(c.get("a"))           # 999
    c.clear()
    print(len(c))               # 0
    print(c.get("missing", 42)) # 42
