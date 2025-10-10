# Problem 5 - cachekit (simple memory cache; root re-export)

**주의: 이 문제도 템플릿 없이 README만 제공됩니다. 학생이 처음부터 파일을 작성하세요.**

## Files (권장)
```
cachekit/
  __init__.py          # VERSION, print_version_info, Cache, __all__
  main.py              # 데모 실행
```

## Goal
아주 단순한 메모리 캐시 작성. 내부적으로 dict를 감싸는 래퍼 클래스 `Cache`를 만들고 루트 API로 제공.

## Why this package exists (동작 원리 & 존재 이유)
파이프라인 중간 결과(전처리/특징 등)를 임시 저장할 때 쓰는 기본 상태 객체를 직접 만들어 보며,
패키지 루트에서 API를 노출하는 패턴 학습.

## Required API
루트 제공:
- `VERSION: str` (예: "1.0")
- `print_version_info() -> None` (간단 출력)
- `class Cache`:
  - `__init__(self) -> None` — 내부 dict 초기화
  - `put(self, key, value) -> None`
  - `get(self, key, default=None)`
  - `__len__(self) -> int`
  - `clear(self) -> None`
- `__all__ = ["Cache", "print_version_info", "VERSION"]`

## Rules
- 내부 구현은 파이썬 dict 사용.
- 라이브러리 내부 함수/메서드에서는 print 지양(테스트 용이성).
- 데모 출력은 `__main__`에서만.

## Examples
```python
from cachekit import Cache, print_version_info
print_version_info()
c = Cache()
c.put("a", 1)
len(c), c.get("a")     # 1, 1
c.clear(); len(c)      # 0
c.get("missing", 42)   # 42
```

## Edge cases (반드시 처리)
- 존재하지 않는 키 조회 시 default 반환
- 동일 키 덮어쓰기 허용
- 길이(`len(cache)`) 정확히 반영

## Instructor quick test
```python
from cachekit import Cache, print_version_info
print_version_info()
c = Cache(); c.put("a", 1); print(len(c), c.get("a"))  # 1 1
c.put("a", 999); print(c.get("a"))                     # 999
c.clear(); print(len(c))                               # 0
print(c.get("missing", 42))                            # 42
```

## Build steps (학생용 가이드)
1. `cachekit/__init__.py`에서 VERSION, print_version_info, Cache 구현 및 `__all__` 설정.
2. `cachekit/main.py`에서 간단 데모:

```python
if __name__ == "__main__":
    from . import Cache, print_version_info
    print_version_info()
    c = Cache(); c.put("a", 1)
    print(len(c), c.get("a"))   # 1 1
    c.clear(); print(len(c))    # 0
```