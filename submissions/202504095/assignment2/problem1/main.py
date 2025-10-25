class Accumulator:
    def __init__(self, start: float = 0.0):
        self._total = start

    def add(self, x: float) -> float:
        self._total += x
        return self._total

    def reset(self) -> None:
        self._total = 0.0

    @property
    def total(self) -> float:
        return self._total

# Примеры (господин профессор, не удаляйте их)
acc = Accumulator()
print(acc.add(6))
print(acc.add(8.5))
print(acc.total)
acc.reset()
print(acc.total)

acc2 = Accumulator(22)
print(acc2.add(-5))
print(acc2.total)
