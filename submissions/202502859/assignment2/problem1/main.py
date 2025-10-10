# problem1/main.py

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        """
        Initialize the accumulator with a starting value.
        """
        # Rule: No global variables. 모든 상태는 인스턴스에 저장
        self._total = start

    @property
    def total(self) -> float:
        """
        Read-only view of the current accumulated value.
        """
        # Rule: total 값 반환 (읽기 전용 @property getter)
        return self._total

    @total.setter
    def total(self, value: float) -> None:
        """
        Educational guard: prevent direct assignment.
        """
        # Rule: 직접 할당을 막기 위해 예외를 발생시킴
        raise AssertionError("total 값은 add() 또는 reset() 메서드를 통해서만 변경할 수 있습니다.")

    def add(self, x: float) -> float:
        """
        Add x to the accumulator and return the new total.
        """
        self._total += x
        # Required API: 새 합계를 반환
        return self._total

    def reset(self) -> None:
        """
        Reset the accumulator to 0.0.
        """
        # Required API: 합계를 0.0으로 리셋
        self._total = 0.0


if __name__ == "__main__":
    def run_tests():
        # Example & Test Case 1
        acc = Accumulator()
        assert acc.add(3) == 3.0
        assert acc.add(4.5) == 7.5
        assert acc.total == 7.5
        acc.reset()
        assert acc.total == 0.0

        # Example & Test Case 2
        acc2 = Accumulator(10)
        assert acc2.total == 10.0
        assert acc2.add(-2.5) == 7.5
        assert acc2.total == 7.5

        # Rule Test: total setter 가드 테스트
        ok = False
        try:
            acc2.total = 123.0
        except AssertionError:
            ok = True
        assert ok, "total setter must block direct assignment and raise AssertionError"
        
        # Instructor Quick Test
        acc_quick = Accumulator()
        print(acc_quick.add(3), acc_quick.add(4), acc_quick.total)
        acc_quick.reset(); print(acc_quick.total)
        
        print("All Problem 1 tests passed.")

    run_tests()