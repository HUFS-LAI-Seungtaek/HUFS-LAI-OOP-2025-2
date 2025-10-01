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
        # TODO: 시작값을 인스턴스 변수에 저장하세요
        # 힌트: self._total = start (private 변수 사용)
        raise NotImplementedError

    @property
    def total(self) -> float:
        """
        Read-only view of the current accumulated value.
        """
        # TODO: 내부 total 값을 반환하세요
        # 힌트: return self._total
        raise NotImplementedError

    @total.setter
    def total(self, value: float) -> None:
        """
        Educational guard: prevent direct assignment.
        """
        # TODO: 직접 할당을 막기 위해 예외를 발생시키세요
        # 힌트: raise AssertionError("적절한 에러 메시지")
        raise NotImplementedError

    def add(self, x: float) -> float:
        """
        Add x to the accumulator and return the new total.
        """
        # TODO: 내부 상태를 업데이트하고 새 합계를 반환하세요
        # 힌트: self._total += x, 그리고 return self._total
        raise NotImplementedError

    def reset(self) -> None:
        """
        Reset the accumulator to 0.0.
        """
        # TODO: 내부 total을 0.0으로 리셋하세요
        # 힌트: self._total = 0.0
        raise NotImplementedError


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

    # run_tests()
    pass