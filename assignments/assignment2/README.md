# Problem 1 - Accumulator (stateful counter for AI pipelines)

## File
`problem1.py`

## Goal
간단한 **Accumulator** 클래스를 만들어, 전역변수 없이 **인스턴스 상태**에 값을 누적·조회·리셋하는 연습을 한다. 실제 AI 파이프라인에서 "처리한 토큰 수, 샘플 수, 총 손실 누적값" 등 **런타임 메트릭**을 추적하는 데 자주 쓰이는 패턴이다.

## Why this class exists (동작 원리 & 존재 이유)
- 동작 원리: 객체가 자신의 내부 상태(누적값)를 갖는다. `add(x)`가 들어올 때마다 내부 상태를 업데이트하고, `total` 프로퍼티로 현재 값을 읽는다. `reset()`은 상태를 0으로 되돌린다.
- 존재 이유: 전역 변수를 쓰면 여러 계산기가 서로 상태를 덮어쓰거나, 테스트하기 어렵다. **객체를 여러 개 만들면 각자 독립된 상태**를 갖는다(예: 데이터셋 A용, B용).

## Required API
- `class Accumulator`
    - `__init__(self, start: float = 0.0)` — 시작값 설정
    - `add(self, x: float) -> float` — x를 더하고 새 합계를 반환
    - `reset(self) -> None` — 합계를 0.0으로 리셋
    - `total` (`@property`, read-only) -> `float` — 현재 합계

## Rules
- **No global variables**; all state must live on the instance.
- read-only `@property`: `total` must be **read-only** (no setter, do not expose internal attribute directly).
- Return types should match the annotations (`float`).

## Examples
```python
acc = Accumulator()
acc.add(3)         # 3.0
acc.add(4.5)       # 7.5
acc.total          # 7.5
acc.reset()
acc.total          # 0.0

acc2 = Accumulator(10)
acc2.add(-2.5)     # 7.5
acc2.total         # 7.5
```

## Instructor quick test
```python
from problem1 import RunningSum
rs = RunningSum()
print(rs.add(3), rs.add(4), rs.total)  # 3 7 7
rs.reset(); print(rs.total)            # 0
```

---

# Problem 2 - textops (clean & tokenize; root re-export, __all__, relative imports)

## Files
다음 파일들을 만들어서 같은 최상위 폴더에 배치하세요(패키지 구조):

```
textops/
  __init__.py          # 루트 API 재노출(re-export) + __all__
  __main__.py          # 데모 실행: python -m textops
  clean/
    __init__.py
    filters.py         # clean_text(s)
  tokenize/
    __init__.py
    word.py            # word_tokens(s)
```

## Goal
간단한 AI/NLP 전처리 패키지 만들기. 텍스트 정규화(`clean_text`) 후 단일 공백 기반 토큰화(`word_tokens`).
사용자는 루트에서 바로 사용:

```python
from textops import clean_text, word_tokens
```

## Why this package exists (동작 원리 & 존재 이유)
- 동작 원리: `clean_text`가 문자열을 표준화 (소문자화 → 앞뒤 공백 제거 → 모든 공백 압축 → 특정 문장부호 제거). `word_tokens`는 이미 정규화된 문자열을 단일 공백으로 분리.
- 존재 이유: 전처리 → 토큰화는 모든 NLP 파이프라인의 기본 빌딩 블록. 패키지 루트에서 API를 노출하면 사용성이 좋아지고 import 경로가 단순해짐.

## Required API
- `clean_text(s: str) -> str` (`clean/filters.py`)
  - 규칙:
    - 전부 소문자
    - 앞뒤 공백 제거
    - 모든 연속 공백(스페이스/탭/개행 등)을 한 칸으로 축약
    - ASCII 문장부호 제거 (단, `'`(apostrophe)과 `-`(hyphen)은 유지)

- `word_tokens(s: str) -> list[str]` (`tokenize/word.py`)
  - 규칙:
    - 단일 공백 기준 분할
    - 빈 문자열/공백뿐이면 `[]` 반환

- 루트(`textops/__init__.py`)에서 재노출 + `__all__ = ["clean_text", "word_tokens"]`
- 내부에서 상대경로 import 사용

## Rules
- 라이브러리 함수 내 print/I/O 금지(순수 함수).
- 전역 가변 상태 금지.
- 예외는 간단 명료한 메시지.

## Examples
```python
from textops import clean_text, word_tokens
s = "  Hello,   WORLD!  "
clean_text(s)                 # "hello world"
word_tokens("hello world")    # ["hello", "world"]
```

## Edge cases (반드시 처리)
- `"\tHello,\nWORLD!!! "` → `"hello world"`
- `"..."` → `""` (모두 제거)
- `"ROCK-'N'-ROLL!!"` → `"rock-'n'-roll"` (`'`, `-` 유지)

## Instructor quick test
```python
from textops import clean_text, word_tokens
print(clean_text(" \tHello,\nWORLD!!!  "))  # "hello world"
print(word_tokens("hello world"))           # ["hello", "world"]
```

---

# Problem 3 - tokenstats (token frequency & top-k, module + __main__ demo)

## File
`problem3_tokenstats.py`

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
import problem3_tokenstats as ts
print(ts.count_tokens(["a","b","a"]))            # {'a':2,'b':1}
print(ts.top_k({"a":2,"b":2,"c":1}, 2))          # [('a',2),('b',2)]
print(ts.merge_freqs([{"a":1},{"a":2,"b":1}]))   # {'a':3,'b':1}
```

---

# Problem 4 - dsops (dataset utilities: split & label stats)

**주의: 이 문제는 템플릿 없이 README만 제공됩니다. 학생이 처음부터 파일/폴더를 직접 생성하세요.**

## Files (권장 구조)
```
dsops/
  __init__.py          # 루트 API 재노출 + __all__
  __main__.py          # python -m dsops 데모
  split/
    __init__.py
    train_test.py      # train_test_split(seq, test_ratio, seed)
  stats/
    __init__.py
    labels.py          # label_distribution(labels)
```

## Goal
리스트만 다루는 토이 버전으로 ML 데이터 유틸 구현:
- Train/Test Split (시드 고정 가능)
- Label 분포 계산

## Why this package exists (동작 원리 & 존재 이유)
프로젝트마다 반복되는 공통 유틸을 패키지로 묶고, 루트에서 바로 쓰게 하는 연습.
시드를 통해 재현 가능한 분할을 만드는 사고방식 학습.

## Required API
- `train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]` (`split/train_test.py`)
  - 검증: `0.0 <= test_ratio <= 1.0` 아니면 `ValueError`
  - 구현:
    - 입력을 복사해 셔플(원본 보존)
    - `seed`가 주어지면 `random.seed(seed)` 후 `random.shuffle(copy)`
    - 컷 인덱스 = `int(round(len(seq) * (1 - test_ratio)))`
    - 앞부분 = train, 뒷부분 = test로 잘라 반환

- `label_distribution(labels: list[str]) -> dict[str, int]` (`stats/labels.py`)
  - 단순 빈도 사전 반환

- 루트(`dsops/__init__.py`)에서 재노출 + `__all__ = ["train_test_split", "label_distribution"]`
- 상대경로 import 사용

## Rules
- 입력 리스트 원본 불변 (copy 후 셔플).
- 예외 메시지는 간단 명료.
- I/O/print 없는 순수 함수.

## Examples
```python
from dsops import train_test_split, label_distribution
train, test = train_test_split([1,2,3,4,5], test_ratio=0.4, seed=42)
label_distribution(["cat","dog","cat"])   # {'cat':2,'dog':1}
```

## Edge cases (반드시 처리)
- `test_ratio=0.0` → test는 `[]`
- `test_ratio=1.0` → train은 `[]`
- 빈 입력 → `([], [])`
- 잘못된 비율(<0 또는 >1) → `ValueError`

## Instructor quick test
```python
from dsops import train_test_split, label_distribution
print(train_test_split(list(range(5)), 0.4, seed=0))   # 재현 가능
print(label_distribution(["a","b","a"]))               # {'a':2,'b':1}
```

---

# Problem 5 - cachekit (simple memory cache; root re-export)

**주의: 이 문제도 템플릿 없이 README만 제공됩니다. 학생이 처음부터 파일을 작성하세요.**

## Files (권장)
```
cachekit/
  __init__.py          # VERSION, print_version_info, Cache, __all__
  __main__.py          # python -m cachekit 데모
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