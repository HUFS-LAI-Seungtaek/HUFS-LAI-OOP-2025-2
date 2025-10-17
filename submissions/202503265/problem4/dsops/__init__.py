"""
dsops: Dataset utilities for ML projects.
Exposes train_test_split and label_distribution at the package root.
"""

from .split.train_test import train_test_split
from .stats.labels import label_distribution

__all__ = ["train_test_split", "label_distribution"]