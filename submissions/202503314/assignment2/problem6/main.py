# main.py
from abc import ABC, abstractmethod


class Metric(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        pass

    def evaluate(self, y_true: list[int], y_pred: list[int]) -> str:
        score = self.compute(y_true, y_pred)
        return f"{self.name}: {score:.3f}"


class Accuracy(Metric):
    def __init__(self) -> None:
        super().__init__("Accuracy")

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        n = len(y_true)
        if n == 0:
            return 0.0
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / n


class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Precision")
        self.positive_class = positive_class

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        tp = sum(1 for t, p in zip(y_true, y_pred)
                 if t == self.positive_class and p == self.positive_class)
        fp = sum(1 for t, p in zip(y_true, y_pred)
                 if t != self.positive_class and p == self.positive_class)
        denom = tp + fp
        if denom == 0:
            return 0.0
        return tp / denom


class Recall(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        tp = sum(1 for t, p in zip(y_true, y_pred)
                 if t == self.positive_class and p == self.positive_class)
        fn = sum(1 for t, p in zip(y_true, y_pred)
                 if t == self.positive_class and p != self.positive_class)
        denom = tp + fn
        if denom == 0:
            return 0.0
        return tp / denom


if __name__ == "__main__":
    def run_tests():
        y_true = [1, 0, 1, 1, 0, 1, 0, 0]
        y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

        accuracy = Accuracy()
        precision = Precision(positive_class=1)
        recall = Recall(positive_class=1)

        assert isinstance(accuracy, Metric)
        assert isinstance(precision, Metric)
        assert isinstance(recall, Metric)

        acc_score = accuracy.compute(y_true, y_pred)
        assert abs(acc_score - 0.75) < 0.01, acc_score

        prec_score = precision.compute(y_true, y_pred)
        assert abs(prec_score - 0.75) < 0.01, prec_score

        rec_score = recall.compute(y_true, y_pred)
        assert abs(rec_score - 0.75) < 0.01, rec_score

        acc_eval = accuracy.evaluate(y_true, y_pred)
        assert "Accuracy: 0.750" in acc_eval, acc_eval

        for metric in [accuracy, precision, recall]:
            result = metric.evaluate(y_true, y_pred)
            assert ":" in result, result

        try:
            Metric("Test")  # type: ignore[abstract]
            assert False
        except TypeError:
            pass

        print("All Problem 6 tests passed.")

    run_tests()