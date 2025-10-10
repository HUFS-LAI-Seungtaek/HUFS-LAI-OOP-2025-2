# dsops/split/__init__.py

# train_test.py 모듈에서 train_test_split 함수를 임포트하여 현재 패키지(split) 레벨로 노출
from .train_test import train_test_split

# 이 패키지에서 외부에 공개할 심볼을 정의 (dsops/__init__.py에서 사용될 예정)
__all__ = ["train_test_split"]