# problem1/main.py
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
        # 시작값을 인스턴스 변수에 저장
        self._total = start

    @property
    def total(self) -> float:
        """
        Read-only view of the current accumulated value.
        """
        # 내부 total 값을 반환
        return self._total

    @total.setter
    def total(self, value: float) -> None:
        """
        Educational guard: prevent direct assignment.
        """
        # 직접 할당을 막기 위해 예외 발생
        raise AssertionError("total property is read-only. Use acc.add(x) or acc.reset() to change the value.")

    def add(self, x: float) -> float:
        """
        Add x to the accumulator and return the new total.
        """
        # 내부 상태를 업데이트하고 새 합계를 반환
        self._total += x
        return self._total

    def reset(self) -> None:
        """
        Reset the accumulator to 0.0.
        """
        # 내부 total을 0.0으로 리셋
        self._total = 0.0


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
        
        # Instructor Quick Test
        acc_test = Accumulator()
        print(acc_test.add(3), acc_test.add(4), acc_test.total)

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