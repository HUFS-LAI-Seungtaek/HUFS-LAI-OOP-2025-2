import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio must be between 0.0 and 1.0")

    n = len(seq)
    if n == 0:
        return [], []

    data = list(seq)  # 원본 보존
    if seed is not None:
        random.seed(seed)
    random.shuffle(data)

    cut = int(round(n * (1 - test_ratio)))
    return data[:cut], data[cut:]

def label_distribution(labels: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for label in labels:
        freq[label] = freq.get(label, 0) + 1
    return freq


if __name__ == "__main__":
    # 데모 실행
    tr, te = train_test_split([1, 2, 3, 4, 5], 0.4, seed=42)
    print(tr, te)   # 항상 같은 결과 (재현성)

    dist = label_distribution(["cat", "dog", "cat"])
    print(dist)     # {'cat': 2, 'dog': 1}
