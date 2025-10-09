# 생성형 AI Gemini 사용범위: 코드 초안 생성, 파이썬 특정 기능과 코드 제안 및 설명 (코드 제안 시 같은 줄에 명시), 작성한 코드 리뷰 요청

import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:

    if not seq:
        return [], []
    if test_ratio < 0.0 or test_ratio > 1.0:
        raise ValueError

    # 입력을 복사해 셔플(원본 보존)
    copy = seq.copy() # 해당 코드를 생성형 AI Gemini를 통해 제안받고 상세한 설명을 요청했습니다.
    # seed가 주어지면 random.seed(seed) 후 random.shuffle(copy)
    if seed is not None:
        random.seed(seed)
    random.shuffle(copy)
    # 컷 인덱스 = int(round(len(seq) * (1 - test_ratio)))
    cut_index = int(round(len(seq) * (1 - test_ratio)))
    
    # 앞부분 = train, 뒷부분 = test로 잘라 반환
    train_set = copy[:cut_index]
    test_set = copy[cut_index:]

    return train_set, test_set
