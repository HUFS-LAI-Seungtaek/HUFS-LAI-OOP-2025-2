# Problem 3 - tokenstats (token frequency & top-k, module + __main__ demo)

## File
`main.py`

## Goal
토큰 리스트에서 빈도 사전을 만들고, 상위 k개를 추출한다. 모듈로 작성하고, `if __name__ == "__main__":` 블록(직접 실행 데모)을 포함한다.

## Why this module exists (동작 원리 & 존재 이유)
- 동작 원리: `count_tokens`가 딕셔너리에 토큰 빈도를 누적. `top_k`가 (빈도 내림차순, 동률은 토큰 이름 오름차순) 정렬 후 상위 k를 슬라이스. (선택) `merge_freqs`는 여러 빈도 맵을 합친다.
- 존재 이유: 코퍼스 탐색/EDA에서 가장 기본이 되는 연산들이며, 정렬 기준/타이브레이커를 명시적으로 코딩하는 연습이 된다. `__main__` 데모는 "임포트 시 부작용 없음, 직접 실행 시만 동작" 패턴 학습에 유용.

## Required API
- `count_tokens(tokens: list[str]) -> dict[str, int]`
- `top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]`
  - 정렬: 빈도 내림차순, 동률은 토큰 문자열 오름차순
  - `k <= 0` 이면 `[]` 반환
- (선택) `merge_freqs(maps: list[dict[str,int]]) -> dict[str,int]`

## Rules
- 표준 라이브러리만 사용.
- 입력이 비어 있어도 안전하게 동작.
- 함수는 순수하게 (print 없음).

## Examples
```python
count_tokens(["a","b","a"])            # {"a":2,"b":1}
top_k({"a":2,"b":2,"c":1}, 2)          # [("a",2),("b",2)]  # 동률은 사전순
merge_freqs([{"a":1},{"a":2,"b":1}])   # {"a":3,"b":1}
```

## Edge cases (반드시 처리)
- `tokens=[]` → `{}`
- `k <= 0` → `[]`
- `k >` 고유토큰수 → 모든 항목
- 동률 정렬 기준: `(–count, token)`

## Instructor quick test
```python
import main as ts
print(ts.count_tokens(["a","b","a"]))            # {'a':2,'b':1}
print(ts.top_k({"a":2,"b":2,"c":1}, 2))          # [('a',2),('b',2)]
print(ts.merge_freqs([{"a":1},{"a":2,"b":1}]))   # {'a':3,'b':1}
```