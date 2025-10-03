"""
dsops: Dataset Operations Package

A lightweight package for common ML dataset utilities:
- Train/test splitting with reproducible seeds
- Label distribution analysis
"""

# 하위 모듈에서 핵심 함수들을 가져와서 루트 레벨에서 사용 가능하게 함
from .split.train_test import train_test_split
from .stats.labels import label_distribution

# 공개 API 정의
__all__ = ["train_test_split", "label_distribution"]

# 패키지 메타데이터
__version__ = "1.0.0"
__author__ = "Student"