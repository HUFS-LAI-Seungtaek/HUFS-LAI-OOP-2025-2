# Problem 1 - Accumulator (stateful counter for AI pipelines)

## File
`main.py`

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
from main import Accumulator
acc = Accumulator()
print(acc.add(3), acc.add(4), acc.total)  # 3.0 7.0 7.0
acc.reset(); print(acc.total)            # 0.0
```