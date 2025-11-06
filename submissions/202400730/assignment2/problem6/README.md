# Problem 6 — 지표 계산기 (상속과 추상화)

**목표**: ML 성능 지표를 계산하는 추상 클래스와 구체 클래스들을 구현하여 상속과 추상화를 학습합니다.

## 문제 설명

머신러닝 모델의 성능을 평가하기 위해 다양한 지표(Metric)가 사용됩니다. 이 문제에서는 추상 클래스 `Metric`과 이를 상속받는 구체 클래스들 `Accuracy`, `Precision`, `Recall`을 구현합니다.

## 요구사항

### 1. 추상 클래스 `Metric`

```python
from abc import ABC, abstractmethod

class Metric(ABC):
    def __init__(self, name: str) -> None:
        # 지표 이름 저장

    @abstractmethod
    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        # 추상 메서드: 구체 클래스에서 구현 필요

    def evaluate(self, y_true: list[int], y_pred: list[int]) -> str:
        # 지표를 계산하고 결과를 문자열로 반환
```

### 2. 구체 클래스 `Accuracy`

```python
class Accuracy(Metric):
    def __init__(self) -> None:
        # 부모 클래스 생성자 호출

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        # 정확도 계산: (맞은 예측 수) / (전체 예측 수)
```

### 3. 구체 클래스 `Precision`

```python
class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        # 양성 클래스 지정 (기본값: 1)

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        # 정밀도 계산: TP / (TP + FP)
```

### 4. 구체 클래스 `Recall`

```python
class Recall(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        # 양성 클래스 지정 (기본값: 1)

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        # 재현율 계산: TP / (TP + FN)
```

## 상세 API 명세

### `Metric.__init__(self, name: str)`
- **목적**: 지표 이름을 저장하는 기본 생성자
- **매개변수**: `name` - 지표의 이름 (예: "Accuracy", "Precision")
- **예시**: `Metric("Custom Metric")`

### `Metric.compute(self, y_true: list[int], y_pred: list[int]) -> float`
- **목적**: 실제값과 예측값을 받아 지표를 계산하는 추상 메서드
- **매개변수**:
  - `y_true` - 실제 레이블 리스트
  - `y_pred` - 예측 레이블 리스트
- **반환값**: 계산된 지표 값 (0.0 ~ 1.0)
- **주의**: 반드시 구체 클래스에서 오버라이드 필요

### `Metric.evaluate(self, y_true: list[int], y_pred: list[int]) -> str`
- **목적**: 지표를 계산하고 결과를 문자열로 반환
- **반환값**: `"{name}: {score:.3f}"` 형식의 문자열
- **예시**: `"Accuracy: 0.750"`

### `Accuracy.compute(self, y_true: list[int], y_pred: list[int]) -> float`
- **목적**: 정확도 계산
- **공식**: `(정확히 예측한 수) / (전체 예측 수)`
- **예시**: `y_true=[1,0,1,1], y_pred=[1,0,0,1]` → `3/4 = 0.75`

### `Precision.compute(self, y_true: list[int], y_pred: list[int]) -> float`
- **목적**: 정밀도 계산
- **공식**: `TP / (TP + FP)`
- **설명**:
  - TP (True Positive): 실제 양성을 양성으로 예측
  - FP (False Positive): 실제 음성을 양성으로 예측
- **예외**: TP + FP = 0인 경우 0.0 반환

### `Recall.compute(self, y_true: list[int], y_pred: list[int]) -> float`
- **목적**: 재현율 계산
- **공식**: `TP / (TP + FN)`
- **설명**:
  - TP (True Positive): 실제 양성을 양성으로 예측
  - FN (False Negative): 실제 양성을 음성으로 예측
- **예외**: TP + FN = 0인 경우 0.0 반환

## 구현 규칙

1. **추상 클래스 사용**: `abc.ABC`와 `@abstractmethod` 데코레이터 사용
2. **상속 구조**: 모든 구체 클래스는 `Metric`을 상속
3. **super() 호출**: 구체 클래스 생성자에서 부모 생성자 호출
4. **타입 힌트**: 모든 메서드에 적절한 타입 힌트 추가
5. **예외 처리**: 나누기 0 상황에서 0.0 반환
6. **입력 검증**: 두 리스트의 길이가 같다고 가정

## 사용 예시

```python
# 지표 객체 생성
accuracy = Accuracy()
precision = Precision(positive_class=1)
recall = Recall(positive_class=1)

# 테스트 데이터
y_true = [1, 0, 1, 1, 0, 1, 0, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

# 개별 지표 계산
print(accuracy.evaluate(y_true, y_pred))    # "Accuracy: 0.750"
print(precision.evaluate(y_true, y_pred))   # "Precision: 0.750"
print(recall.evaluate(y_true, y_pred))      # "Recall: 0.750"

# 다형성 활용
metrics = [accuracy, precision, recall]
for metric in metrics:
    result = metric.evaluate(y_true, y_pred)
    print(result)

# 추상 클래스 직접 인스턴스화 불가
# metric = Metric("Test")  # TypeError 발생
```

## 계산 예시

**데이터**: `y_true = [1, 0, 1, 1]`, `y_pred = [1, 0, 0, 1]`

### Accuracy 계산:
- 정확한 예측: 인덱스 0, 1, 3 → 3개
- 전체 예측: 4개
- Accuracy = 3/4 = 0.75

### Precision 계산 (positive_class=1):
- TP: 실제 1을 1로 예측 → 인덱스 0, 3 → 2개
- FP: 실제 0을 1로 예측 → 0개
- Precision = 2/(2+0) = 1.0

### Recall 계산 (positive_class=1):
- TP: 실제 1을 1로 예측 → 인덱스 0, 3 → 2개
- FN: 실제 1을 0으로 예측 → 인덱스 2 → 1개
- Recall = 2/(2+1) = 0.667

## 엣지 케이스

1. **빈 리스트**: 두 리스트가 모두 빈 경우 → 0.0 반환
2. **모든 예측이 틀린 경우**: Accuracy = 0.0
3. **분모가 0인 경우**: Precision/Recall에서 해당 클래스가 없는 경우 → 0.0 반환
4. **이진 분류**: 0과 1만 포함된 경우
5. **다중 클래스**: positive_class가 아닌 값들은 모두 음성으로 처리

## 학습 목표

- **추상화**: 공통 인터페이스를 정의하고 구체 구현을 분리
- **상속**: 코드 재사용과 계층 구조 이해
- **다형성**: 같은 인터페이스로 다른 동작 수행
- **실용성**: 실제 ML에서 사용되는 지표 계산
- **타입 시스템**: ABC와 abstractmethod 활용

## 힌트

- `from abc import ABC, abstractmethod` 임포트 필요
- TP, FP, TN, FN을 직접 계산해보세요
- 나누기 전에 분모가 0인지 확인하세요
- `evaluate` 메서드는 `compute`를 호출하여 구현
- 리스트 컴프리헨션을 활용하면 간결하게 작성 가능