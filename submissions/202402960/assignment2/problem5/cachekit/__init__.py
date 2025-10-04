VERSION = "1.0"

def print_version_info() -> None:
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self) -> None:
        self.store = {}

    def put(self, key, value) -> None:
        self.store[key] = value

    def get(self, key, default=None):
        return self.store.get(key, default)
    
    def __len__(self) -> int:
        return len(self.store)
    
    def clear(self) -> None:
        self.store.clear()

__all__ = ["Cache", "print_version_info","VERSION"]