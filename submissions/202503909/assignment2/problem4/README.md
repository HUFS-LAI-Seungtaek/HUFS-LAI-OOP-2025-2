# Problem 4 - dsops (dataset utilities: split & label stats)

**주의: 이 문제는 템플릿 없이 README만 제공됩니다. 학생이 처음부터 파일/폴더를 직접 생성하세요.**

## Files (권장 구조)
```
dsops/
  __init__.py          # 루트 API 재노출 + __all__
  main.py              # 데모 실행
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

## Build steps (학생용 가이드)
1. 위 폴더 구조를 그대로 생성.
2. `split/train_test.py`와 `stats/labels.py`에 함수를 구현.
3. `dsops/__init__.py`에서 두 함수를 재노출하고 `__all__` 정의.
4. `dsops/main.py`를 만들어 데모 실행 가능하게:

```python
if __name__ == "__main__":
    from . import train_test_split, label_distribution
    tr, te = train_test_split([1,2,3,4,5], 0.4, seed=42)
    print(tr, te)
    print(label_distribution(["cat","dog","cat"]))
```