import random
from typing import List, Tuple, Optional, Dict, Any
from collections import Counter

def train_test_split(seq: List, test_ratio: float, seed: Optional[int] = None) -> Tuple[list, list]:
   
    # Проверка на валидность test_ratio
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio должен быть между 0.0 и 1.0.")

    copied_seq = seq.copy()

    # Установка сида для воспроизводимости
    if seed is not None:
        random.seed(seed)
    
    # Перемешивание, если список не пуст
    if copied_seq:
        random.shuffle(copied_seq)
        
    cut_index = int(round(len(copied_seq) * (1.0 - test_ratio)))

    # Разделение
    train = copied_seq[:cut_index]
    test = copied_seq[cut_index:]
    
    return train, test

def label_distribution(labels: List[Any]) -> Dict[Any, int]:

    return dict(Counter(labels))

if __name__ == "__main__":
    print("--- Демонстрация train_test_split ---")
    data = [1, 2, 3, 4, 5]
    ratio = 0.4
    seed_value = 42
    tr, te = train_test_split(data, test_ratio=ratio, seed=seed_value)
    
    print(f"Исходный список: {data}")
    print(f"Разделение (test_ratio={ratio}, seed={seed_value}):")
    print(f"  Train: {tr}")
    print(f"  Test: {te}")
    print(f"  Проверка: len(Train)={len(tr)}, len(Test)={len(te)}")
    
    print("\n--- Быстрый тест 1 (Воспроизводимость) ---")
    # Ожидаемый вывод: ([2, 4, 0], [3, 1]) или подобный, но фиксированный для seed=0
    print(train_test_split(list(range(5)), 0.4, seed=0))

    print("\n--- Проверка краевых случаев (train_test_split) ---")
    # test_ratio=0.0 -> test=[]
    print(f"0.0 ratio: {train_test_split([1, 2, 3], 0.0)}")
    # test_ratio=1.0 -> train=[]
    print(f"1.0 ratio: {train_test_split([1, 2, 3], 1.0)}")
    # Пустой ввод
    print(f"Пустой ввод: {train_test_split([], 0.5)}")
    # Неверное соотношение
    try:
        train_test_split([1], 1.1)
    except ValueError as e:
        print(f"Ошибка ValueError: {e}")

    print("\n--- Демонстрация label_distribution ---")
    labels = ["cat", "dog", "cat", "fish", "dog", "cat"]
    dist = label_distribution(labels)
    print(f"Список меток: {labels}")
    print(f"Распределение: {dist}")

    print("\n--- Быстрый тест 2 (Распределение меток) ---")
    # Ожидаемый вывод: {'a': 2, 'b': 1}
    print(label_distribution(["a", "b", "a"]))

