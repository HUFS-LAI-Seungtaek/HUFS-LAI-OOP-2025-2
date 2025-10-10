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
        if not y_true or not y_pred:
            return 0.0
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_pred)

class Precision(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Precision")
        self.positive_class = positive_class 

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        TP = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p == self.positive_class)
        FP = sum(1 for t, p in zip(y_true, y_pred) if t != self.positive_class and p == self.positive_class)
        if TP + FP == 0:
            return 0.0
        return TP / (TP + FP)

class Recall(Metric):
    def __init__(self, positive_class: int = 1) -> None:
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: list[int], y_pred: list[int]) -> float:
        TP = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p == self.positive_class)
        FN = sum(1 for t, p in zip(y_true, y_pred) if t == self.positive_class and p != self.positive_class)
        if TP + FN == 0:
            return 0.0
        return TP / (TP + FN)

if __name__ == "__main__":
    # -------------------------------
    # Student self-checks (uncomment)
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
        assert isinstance(accuracy, Metric), "Accuracy should inherit from Metric"
        assert isinstance(precision, Metric), "Precision should inherit from Metric"
        assert isinstance(recall, Metric), "Recall should inherit from Metric"

        # 정확도 테스트 (6/8 = 0.75)
        acc_score = accuracy.compute(y_true, y_pred)
        assert abs(acc_score - 0.75) < 0.01, f"Accuracy should be 0.75, got {acc_score}"

        # 정밀도 테스트 (TP=3, FP=1, Precision=3/4=0.75)
        prec_score = precision.compute(y_true, y_pred)
        assert abs(prec_score - 0.75) < 0.01, f"Precision should be 0.75, got {prec_score}"

        # 재현율 테스트 (TP=3, FN=1, Recall=3/4=0.75)
        rec_score = recall.compute(y_true, y_pred)
        assert abs(rec_score - 0.75) < 0.01, f"Recall should be 0.75, got {rec_score}"

        # evaluate 메서드 테스트
        acc_eval = accuracy.evaluate(y_true, y_pred)
        assert "Accuracy: 0.750" in acc_eval, f"Accuracy evaluate format wrong: {acc_eval}"

        # 다형성 테스트
        metrics = [accuracy, precision, recall]
        for metric in metrics:
            result = metric.evaluate(y_true, y_pred)
            assert ":" in result, f"Evaluate result should contain colon: {result}"

        # 추상 클래스 직접 인스턴스화 불가 테스트
        try:
            metric = Metric("Test")
            assert False, "Should not be able to instantiate abstract class"
        except TypeError:
            pass  # Expected

        print("All Problem 6 tests passed.")
 
    #run_tests()
    #pass