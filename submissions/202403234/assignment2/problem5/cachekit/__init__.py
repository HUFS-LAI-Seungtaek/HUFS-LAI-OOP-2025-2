VERSION="1.0"
def print_version_info():
    print(f"version:{VERSION}")

class Cache():
    def __init__(self):
       self._store={}
    
    def put(self, key, value):
       self._store[key]=value
       
    def get(self, key, default=None):
       return self._store.get(key,default)
    def __len__(self):
       return len(self._store)
    def clear(self):
        self._store.clear()

__all__ = ["Cache", "print_version_info", "VERSION"]