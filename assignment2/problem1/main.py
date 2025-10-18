# problem1.py
"""
Problem 1 — Accumulator (stateful counter for AI pipelines)

- 전역 변수 없이 누적 합계를 추적하는 클래스
- 읽기 전용 프로퍼티(@property)와 setter 보호를 통해 잘못된 사용 방지
"""

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        """
        초기값으로 누적 합계를 설정합니다.
        
        Args:
            start (float): 누적 합계의 시작값 (기본값 0.0)
        """
        # private 변수로 내부 상태를 관리
        self._total = start

    @property
    def total(self) -> float:
        """
        현재 누적 합계를 읽기 전용으로 반환합니다.

        Returns:
            float: 현재 누적 합계
        """
        return self._total

    @total.setter
    def total(self, value: float) -> None:
       
        raise AssertionError("total은 직접 수정할 수 없습니다. add() 또는 reset()을 사용하세요.")

    def add(self, x: float) -> float:
        
        self._total += x
        return self._total

    def reset(self) -> None:
        """
        누적 합계를 0.0으로 초기화합니다.
        """
        self._total = 0.0


if __name__ == "__main__":
  
    def run_tests():
        # 기본 생성자 테스트
        acc = Accumulator()
        assert acc.add(3) == 3.0
        assert acc.add(4.5) == 7.5
        assert acc.total == 7.5
        acc.reset()
        assert acc.total == 0.0

        # 초기값 지정 테스트
        acc2 = Accumulator(10)
        assert acc2.total == 10.0
        assert acc2.add(-2.5) == 7.5
        assert acc2.total == 7.5

        # total setter 보호 테스트
        ok = False
        try:
            acc2.total = 123.0
        except AssertionError:
            ok = True
        assert ok, "total setter는 직접 할당을 막아야 합니다."

        print("All Problem 1 tests passed.")

    run_tests()
