VERSION = "1.0"

__all__ = ["Cache", "print_version_info", "VERSION"]

def print_version_info() -> None:
    print(f'cacheckit version: {VERSION}')

class Cache:
    def __init__(self) -> None:
        self._data = {}

    def put(self, key, value) -> None:
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __len__(self) -> int:
        return len(self._data)

    def clear(self) -> int:
        count = len(self._data)
        self._data.clear()
        return count

print_version_info()
c = Cache(); c.put("a", 1); print(len(c), c.get("a"))  # 1 1
c.put("a", 999); print(c.get("a"))                     # 999
c.clear(); print(len(c))                               # 0
print(c.get("missing", 42))                            # 42