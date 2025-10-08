VERSION = "1.0"

def print_version_info():
    print(f"cachekit version {VERSION}")

class Cache:
    def __init__(self):
        self.data = {}
    def put(self, key, value):
        self.data[key] = value
    def get(self, key, default=None):
        return self.data.get(key, default)
    def clear(self):
        self.data.clear()
    def __len__(self):
        return len(self.data)
    
__all__ = ["Cache", "print_version_info", "VERSION"]
