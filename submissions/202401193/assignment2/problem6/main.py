# main.py
"""
Problem 6 — 지표 계산기 (상속과 추상화)
- ML 성능 지표를 계산하는 추상 클래스와 구체 클래스들 구현
- 상속, 추상화, 다형성 학습
"""

from abc import ABC, abstractmethod


class Metric(ABC):
    def __init__(self, name: str) -> None:
        """
        지표 이름을 저장하는 기본 생성자.
        """
        # TODO: 지표 이름을 인스턴스 변수에 저장하세요
        # 힌트: self.name = name
        self.name = name

    @abstractmethod
    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        """
        실제값과 예측값을 받아 지표를 계산하는 추상 메서드.
        구체 클래스에서 반드시 구현해야 합니다.
        """
        # TODO: 추상 메서드이므로 구현하지 않음
        # 힌트: pass 또는 raise NotImplementedError
        pass

    def evaluate(self, y_true: list[int], y_pred: list[int]) -> str:
        """
        지표를 계산하고 결과를 문자열로 반환.
        """
        # TODO: compute 메서드를 호출하여 지표를 계산하고 문자열로 반환하세요
        # 힌트:
        # 1) score = self.compute(y_true, y_pred)
        # 2) return f"{self.name}: {score:.3f}"
        score: float = self.compute(y_true, y_pred)
        return f"{self.name}: {score:.3f}"


class Accuracy(Metric):
    def __init__(self) -> None:
        """
        정확도 지표 초기화.
        """
        # TODO: 부모 클래스 생성자를 호출하세요
        # 힌트: super().__init__("Accuracy")
        super().__init__("Accuracy")

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        """
        정확도 계산: (맞은 예측 수) / (전체 예측 수)
        """
        # TODO: 정확도를 계산하세요
        # 힌트:
        # 1) 빈 리스트인 경우 0.0 반환
        total_samples: int = len(y_true)
        if total_samples == 0:
            return 0.0
        # 2) correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        correct_predictions: int = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        # 3) return correct / len(y_true)
        accuracy: float = correct_predictions / total_samples
        return accuracy


class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        """
        정밀도 지표 초기화.
        """
        # TODO: 부모 클래스 생성자 호출과 양성 클래스 저장
        # 힌트:
        # 1) super().__init__("Precision")
        super().__init__("Precision")
        # 2) self.positive_class = positive_class
        self.positive_class = positive_class

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        """
        정밀도 계산: TP / (TP + FP)
        """
        # TODO: 정밀도를 계산하세요
        # 힌트:
        # 1) TP = 실제 양성을 양성으로 예측한 수
        TP: int = sum(
            1 for t, p in zip(y_true, y_pred)
            if t == self.positive_class and p == self.positive_class
        )
        # 2) FP = 실제 음성을 양성으로 예측한 수
        FP: int = sum(
            1 for t, p in zip(y_true, y_pred)
            if t != self.positive_class and p == self.positive_class
        )
        # 3) 분모가 0이면 0.0 반환
        denominator: int = TP + FP
        if denominator == 0:
            return 0.0

        # 4) TP = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p == self.positive_class)
        precision: float = TP / denominator
        # 5) FP = sum(1 for t, p in zip(y_true, y_pred) if t != self.positive_class and p == self.positive_
