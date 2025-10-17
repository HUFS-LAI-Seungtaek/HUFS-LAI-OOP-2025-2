# dsops/__init__.py

# 상대 경로 임포트를 사용하여 함수 재노출
from .split.train_test import train_test_split
from .stats.labels import label_distribution

# __all__ 리스트로 외부 공개 API 명시
__all__ = ["train_test_split", "label_distribution"]