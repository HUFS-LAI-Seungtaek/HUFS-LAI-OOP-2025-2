from abc import ABC, abstractmethod
from typing import List

# --- Абстрактный класс ---

class Metric(ABC):
    
    def __init__(self, name: str) -> None:
      
        self.name = name

    @abstractmethod
    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
      
        pass

    def evaluate(self, y_true: List[int], y_pred: List[int]) -> str:
     
        score = self.compute(y_true, y_pred)
        return f"{self.name}: {score:.3f}"

# --- Вспомогательная функция для TP, FP, FN ---

def _calculate_confusion_matrix_components(
    y_true: List[int], y_pred: List[int], positive_class: int
) -> tuple[int, int, int]:
   
    TP = 0  # True Positive: Фактически P, предсказано P
    FP = 0  # False Positive: Фактически N, предсказано P
    FN = 0  # False Negative: Фактически P, предсказано N
    
    for true, pred in zip(y_true, y_pred):
        is_true_positive = (true == positive_class)
        is_pred_positive = (pred == positive_class)
        
        if is_true_positive and is_pred_positive:
            TP += 1
        elif not is_true_positive and is_pred_positive:
            FP += 1
        elif is_true_positive and not is_pred_positive:
            FN += 1
            
    return TP, FP, FN

# --- Конкретные классы ---

class Accuracy(Metric):
   
    def __init__(self) -> None:
        # Вызов конструктора родительского класса
        super().__init__("Accuracy")

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
        """
        Вычисляет Точность.
        """
        if not y_true:
            # Обработка пустого списка
            return 0.0

        # Количество правильных предсказаний
        correct_predictions = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
        total_predictions = len(y_true)
        
        return correct_predictions / total_predictions

class Precision(Metric):
   
    def __init__(self, positive_class: int = 1) -> None:
      
        super().__init__("Precision")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
      
        if not y_true:
             return 0.0

        TP, FP, _ = _calculate_confusion_matrix_components(y_true, y_pred, self.positive_class)
        
        denominator = TP + FP # Общее количество предсказаний как положительный класс
        
        if denominator == 0:
            # Обработка деления на ноль (если ничто не было предсказано как положительный класс)
            return 0.0
            
        return TP / denominator

class Recall(Metric):
   
    def __init__(self, positive_class: int = 1) -> None:
       
        super().__init__("Recall")
        self.positive_class = positive_class

    def compute(self, y_true: List[int], y_pred: List[int]) -> float:
       
        if not y_true:
            return 0.0

        TP, _, FN = _calculate_confusion_matrix_components(y_true, y_pred, self.positive_class)
        
        denominator = TP + FN # Общее количество фактических положительных меток
        
        if denominator == 0:
            # Обработка деления на ноль (если в фактических данных нет положительного класса)
            return 0.0
            
        return TP / denominator


if __name__ == "__main__":
    # Создание объектов метрик
    accuracy = Accuracy()
    precision = Precision(positive_class=1)
    recall = Recall(positive_class=1)

    # Тестовые данные
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

    # --- Использование полиморфизма ---
    print("--- Результаты метрик ---")

    metrics: List[Metric] = [accuracy, precision, recall]

    # Единый интерфейс evaluate() для разных классов метрик (полиморфизм)
    for metric in metrics:
        result = metric.evaluate(y_true, y_pred)
        print(result)

    print("-------------------------")
