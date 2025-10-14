# problem1.py
"""
Problem 1 — Accumulator (stateful counter for AI pipelines)
- Track a running sum without global variables.
- Educate: @property (read-only) + guarded setter that blocks misuse.
"""

# gpt 사용
# @가 무슨 역할을 하는지 이해하지 못하여 copilot에게 개념에 대한 내용을 물어보았습니다.
# 에러 메시지를 발생시키기 위한 방법과 이에 따른 run_test()에 관한 내용에 대해 도움받았습니다.
# try, except, ok, assert 에 대한 개념에 대해 물어보았습니다.

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        self._total = start

    @property
    def total(self) -> float:
        return self._total
        
    @total.setter
    def total(self, value: float) -> None:
        raise AssertionError("직접 할당은 불가합니다.")

    def add(self, x: float) -> float:
        self._total += x
        return self._total

    def reset(self) -> None:
        self._total = 0.0
        return self._total

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

    #run_tests()
    pass