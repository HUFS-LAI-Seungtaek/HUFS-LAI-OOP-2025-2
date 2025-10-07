import random

def train_test_split(seq: list, test_ratio: float, seed: int | None = None) -> tuple[list, list]:
    if 0.0 <= test_ratio <= 1.0:
        copy = seq.copy()

        if seed is not None:
            random.seed(seed)
        random.shuffle(copy)

        cut_index = int(round(len(seq) * (1 - test_ratio)))

        train = copy[:cut_index]
        test = copy[cut_index:]

        return train, test
    
    else:
        raise ValueError("test_ratio must be between 0.0 and 1.0.")

'''
원본 보존하면서 복사하는 방법: https://wikidocs.net/214904 
데이터가 입력되었는지 확인하는 방법은 제미나이에게 물어봤습니다.
random.seed()에 대한 정보 공부: https://m.blog.naver.com/regenesis90/222363064500
int(round(len(seq) * (1 - test_ratio))) 이 줄이 이해 안돼서 제미나이한테 설명 부탁했습니다.
'''