class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        self._total = float(start)

    @property
    def total(self) -> float:
        return self._total

    @total.setter
    def total(self, value: float) -> None:
        raise AssertionError("Cannot set total directly. Use add() or reset().")

    def add(self, x: float) -> float:
        self._total += float(x)
        return self._total

    def reset(self) -> None:
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


 '''credit:@property와 @setter를 활용하여 속성을 읽기 전용으로 만드는 방법,  
직접 할당을 막는 예외 처리 방식,  
그리고 `assert` 문을 사용한 테스트 코드 작성 방식에 대해  
chat gpt로부터 개념적 설명과 코드 동작 원리에 대한 조언을 참고하였습니다.'''

