# dsops/stats/__init__.py

# labels.py 모듈에서 label_distribution 함수를 임포트하여 현재 패키지(stats) 레벨로 노출
from .labels import label_distribution

# 이 패키지에서 외부에 공개할 심볼을 정의 (dsops/__init__.py에서 사용될 예정)
__all__ = ["label_distribution"]