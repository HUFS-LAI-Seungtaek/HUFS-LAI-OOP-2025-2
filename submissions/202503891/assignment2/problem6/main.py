from abc import ABC, abstractmethod
from typing import List

class Metric(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        pass

    def evaluate(self, y_true: List[int], y_pred: List[int]) -> str:
        score = self.compute(y_true, y_pred)
        return f"{self.name}: {score:.3f}"

class Accuracy(Metric):
    def __init__(self) -> None:
        super().__init__("Accuracy")

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        if not y_true:
            return 0.0
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)

class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Precision")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p == self.positive_class)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t != self.positive_class and p == self.positive_class)
        return tp / (tp + fp) if (tp + fp) > 0 else 0.0

class Recall(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p == self.positive_class)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p != self.positive_class)
        return tp / (tp + fn) if (tp + fn) > 0 else 0.0

if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

    accuracy = Accuracy()
    precision = Precision(positive_class=1)
    recall = Recall(positive_class=1)

    print(accuracy.evaluate(y_true, y_pred))
    print(precision.evaluate(y_true, y_pred))
    print(recall.evaluate(y_true, y_pred))

    metrics = [accuracy, precision, recall]
    for metric in metrics:
        print(metric.evaluate(y_true, y_pred))

'''credit:Accuracy, Precision, Recall 클래스를 구현할 때 상속 구조와 추상 클래스 사용 방식에 대해
ChatGPT의 설명을 참고하였습니다.'''
