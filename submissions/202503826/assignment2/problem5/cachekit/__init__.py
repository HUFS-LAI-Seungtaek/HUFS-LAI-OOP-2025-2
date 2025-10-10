VERSION = "1.0"

def print_version_info():
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]     #박영재 학우님의 코드를 참조했습니다.
        return default
    
    def clear(self):
        self.data.clear()

    def __len__(self):
        return len(self.data)
    
__all__ = ["Cache", "print_version_info", "VERSION"]
