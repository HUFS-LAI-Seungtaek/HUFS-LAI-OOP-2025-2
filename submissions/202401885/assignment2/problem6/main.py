"""
Problem 6 — 지표 계산기 (상속과 추상화)
- ML 성능 지표를 계산하는 추상 클래스와 구체 클래스들 구현
- 상속, 추상화, 다형성 학습
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Metric(ABC):
    def __init__(self, name: str) -> None:
        """지표 이름을 저장하는 기본 생성자."""
        self.name = name

    @abstractmethod
    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        """실제값과 예측값을 받아 지표를 계산(구체 클래스에서 구현)."""
        raise NotImplementedError

    def evaluate(self, y_true: List[int], y_pred: List[int]) -> str:
        """지표를 계산하고 결과를 문자열로 반환."""
        score = self.compute(y_true, y_pred)
        return f"{self.name}: {score:.3f}"


class Accuracy(Metric):
    def __init__(self) -> None:
        """정확도 지표 초기화."""
        super().__init__("Accuracy")

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        """정확도 = (맞은 예측 수) / (전체 예측 수)"""
        n = len(y_true)
        if n == 0:
            return 0.0
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / n


class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        """정밀도 지표 초기화."""
        super().__init__("Precision")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        """정밀도 = TP / (TP + FP)"""
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
        """재현율 지표 초기화."""
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        """재현율 = TP / (TP + FN)"""
        tp = sum(1 for t, p in zip(y_true, y_pred)
                 if t == self.positive_class and p == self.positive_class)
        fn = sum(1 for t, p in zip(y_true, y_pred)
                 if t == self.positive_class and p != self.positive_class)
        denom = tp + fn
        if denom == 0:
            return 0.0
        return tp / denom


if __name__ == "__main__":
    # -------------------------------
    # Student self-checks
    # -------------------------------
    def run_tests():
        # 테스트 데이터
        y_true = [1, 0, 1, 1, 0, 1, 0, 0]
        y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

        # 지표 객체 생성
        accuracy = Accuracy()
        precision = Precision(positive_class=1)
        recall = Recall(positive_class=1)

        # 상속 확인
        assert isinstance(accuracy, Metric)
        assert isinstance(precision, Metric)
        assert isinstance(recall, Metric)

        # 정확도(6/8=0.75), 정밀도(3/(3+1)=0.75), 재현율(3/(3+1)=0.75)
        acc_score = accuracy.compute(y_true, y_pred)
        prec_score = precision.compute(y_true, y_pred)
        rec_score = recall.compute(y_true, y_pred)
        assert abs(acc_score - 0.75) < 1e-6, acc_score
        assert abs(prec_score - 0.75) < 1e-6, prec_score
        assert abs(rec_score - 0.75) < 1e-6, rec_score

        # evaluate 형식
        assert accuracy.evaluate(y_true, y_pred) == "Accuracy: 0.750"
        assert precision.evaluate(y_true, y_pred) == "Precision: 0.750"
        assert recall.evaluate(y_true, y_pred) == "Recall: 0.750"

        print("All Problem 6 tests passed.")

    run_tests()
