"""
Train/Test splitting utilities for dataset preparation.
"""
import random


def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    """
    데이터를 훈련용과 테스트용으로 분할합니다.
    
    Args:
        seq: 분할할 데이터 리스트
        test_ratio: 테스트 데이터 비율 (0.0 ~ 1.0)
        seed: 재현성을 위한 랜덤 시드 (None이면 시드 설정 안함)
        
    Returns:
        (train_data, test_data) 튜플
        
    Raises:
        ValueError: test_ratio가 0.0~1.0 범위를 벗어날 때
    """
    # 비율 검증
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError(f"test_ratio must be between 0.0 and 1.0, got {test_ratio}")
    
    # 빈 리스트 처리
    if not seq:
        return [], []
    
    # 원본 보존을 위한 복사
    data_copy = seq.copy()
    
    # 시드가 주어지면 설정 후 셔플
    if seed is not None:
        random.seed(seed)
    random.shuffle(data_copy)
    
    # 분할 지점 계산
    total_size = len(data_copy)
    train_size = int(round(total_size * (1 - test_ratio)))
    
    # 분할 실행
    training_data = data_copy[:train_size]
    testing_data = data_copy[train_size:]
    
    return training_data, testing_data