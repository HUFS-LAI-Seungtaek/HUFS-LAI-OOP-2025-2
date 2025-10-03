# problem1.py
"""
Problem 1 — Accumulator (stateful counter for AI pipelines)
- Track a running sum without global variables.
- Educate: @property (read-only) + guarded setter that blocks misuse.
"""

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        """
        Initialize the accumulator with a starting value.
        """
        # TODO: store the starting value on the instance (float)
        self._value = float(start)

    @property
    def total(self) -> float:
        """
        Read-only view of the current accumulated value.
        """
        # TODO: return the internal total
        return float(self._value)

    @total.setter
    def total(self, value: float) -> None:
        """
        Educational guard: prevent direct assignment.
        """
        # TODO: raise AssertionError (or AttributeError) with a helpful message
        raise AssertionError("Direct assignment is prohibited")

    def add(self, x: float) -> float:
        """
        Add x to the accumulator and return the new total.
        """
        # TODO: update internal state and return it
        self._value += x
        return float(self._value)

    def reset(self) -> None:
        """
        Reset the accumulator to 0.0.
        """
        # TODO: set internal total to 0.0
        self._value = 0.0
        

if __name__ == "__main__":
    # -------------------------------
    # Student self-checks (uncomment)
    # -------------------------------
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