# problem1.py

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        
        self.finaltotal = start

    @property
    def total(self) -> float:
        
        return self.finaltotal

    @total.setter
    def total(self, value: float) -> None:
        raise AssertionError
        

    def add(self, x: float) -> float:
       
        self.finaltotal += x
        return self.finaltotal

    def reset(self) -> None:
        
        self.finaltotal=0.0


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
    pass
