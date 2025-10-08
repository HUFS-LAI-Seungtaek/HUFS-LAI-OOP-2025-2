class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        """
        Initialize the accumulator with a starting value.
        """
        self._total = float(start)

    @property
    def total(self) -> float:
        """
        Read-only view of the current accumulated value.
        """
        return self._total

    @total.setter
    def total(self, value: float) -> None:
        """
        Educational guard: prevent direct assignment.
        """
        raise AssertionError("Direct assignment to 'total' is not allowed. Use add() or reset().")

    def add(self, x: float) -> float:
        """
        Add x to the accumulator and return the new total.
        """
        self._total += float(x)
        return self._total

    def reset(self) -> None:
        """
        Reset the accumulator to 0.0.
        """
        self._total = 0.0


if __name__ == "__main__":
    def run_tests():
        acc = Accumulator()
        assert acc.add(3) == 3.0
        assert acc.add(4.5) == 7.5
        assert acc.total == 7.5
        acc.reset()
        assert acc.total == 0.0

        acc2 = Accumulator(10)
        assert acc2.total == 10.0
        assert acc2.add(-2.5) == 7.5
        assert acc2.total == 7.5

        ok = False
        try:
            acc2.total = 123.0
        except AssertionError:
            ok = True
        assert ok, "total setter must block direct assignment"

        print("All Problem 1 tests passed.")

    run_tests()
