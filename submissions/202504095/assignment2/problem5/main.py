# cachekit/__init__.py

VERSION = "1.0"

def print_version_info():
    print(f"Cachekit (Простой in-memory кэш) - Версия: {VERSION}")

class Cache:
    def __init__(self):
        """Инициализирует внутренний словарь для хранения кэша."""
        # Используем dict для внутреннего хранения
        self._cache = {}

    def put(self, key, value):
        self._cache[key] = value

    def get(self, key, default=None):
        # Используем метод get словаря для обработки отсутствующих ключей
        return self._cache.get(key, default)

    def clear(self):
        self._cache.clear()

    def __len__(self):
        return len(self._cache)

    def __repr__(self):
        return f"<Cache with {len(self)} items>"

# Определяем API, который будет экспортироваться при 'from cachekit import *'
__all__ = ["Cache", "print_version_info", "VERSION"]
