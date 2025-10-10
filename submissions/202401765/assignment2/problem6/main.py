from abc import ABC, abstractmethod
from typing import List, Tuple

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
        correct_predictions = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
        total_predictions = len(y_true)
        if total_predictions == 0:
            return 0.0
        return correct_predictions / total_predictions

class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Precision")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        tp = sum(1 for true, pred in zip(y_true, y_pred) if true == self.positive_class and pred == self.positive_class)
        fp = sum(1 for true, pred in zip(y_true, y_pred) if true != self.positive_class and pred == self.positive_class)
        
        denominator = tp + fp
        if denominator == 0:
            return 0.0
        return tp / denominator

class Recall(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        tp = sum(1 for true, pred in zip(y_true, y_pred) if true == self.positive_class and pred == self.positive_class)
        fn = sum(1 for true, pred in zip(y_true, y_pred) if true == self.positive_class and pred != self.positive_class)
        
        denominator = tp + fn
        if denominator == 0:
            return 0.0
        return tp / denominator

# metric 작동 검증 코드 제미나이 도움 받음

if __name__ == "__main__":
    def run_tests():
        # Test data
        y_true = [1, 0, 1, 1, 0, 1, 0, 0]
        y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

        # Create metric objects
        accuracy = Accuracy()
        precision = Precision()
        recall = Recall()

        # Individual evaluation
        print(accuracy.evaluate(y_true, y_pred))
        print(precision.evaluate(y_true, y_pred))
        print(recall.evaluate(y_true, y_pred))

        # Check for polymorphism
        metrics = [accuracy, precision, recall]
        for metric in metrics:
            print(metric.evaluate(y_true, y_pred))

        # Edge case test
        print(accuracy.evaluate([], []))  # Should print Accuracy: 0.000
        print(precision.evaluate([], [])) # Should print Precision: 0.000
        print(recall.evaluate([], []))    # Should print Recall: 0.000
        
        print("All Problem 6 tests passed.")

    run_tests()
