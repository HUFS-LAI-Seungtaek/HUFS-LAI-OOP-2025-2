# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""

def count_tokens(tokens: list[str]) -> dict[str, int]:
    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1
    return d

'''
힌트대로 따라 만들었는데 .get()의 두번 째 인자가 무엇을 의미하는지 모르겠어서
https://junior-datalist.tistory.com/203 를 참고했습니다.
'''

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    else:
        freqs = list(freqs.items())
        sorted(freqs, key = lambda x: (-x[1], x[0]))
        return freqs[:k]

'''
입력은 dict 고 반환은 list 라는 걸 처음에 모르고 돌렸다가 오류나서 다시보니 일단 타입을 바꿔야 하는구나를 알았고
dict 를 list로 변환하는 방법은 https://codechacha.com/ko/python-convert-dict-to-list/ 에서 배웠습니다.
sorted()와 key 매개변수에 대해서 강의자료를 참조했지만 고려 기준을 여러개 적는 방법이 따로 안 나와 있어서
여러개의 경우 어떻게 하는지 제미나이한테 물어봤습니다.
'''

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for freq_dict in maps:
        for key, value in freq_dict.items():
            result[key] = result.get(key, 0) + value
    return result
    
'''
딕셔너리에서 키가 같을 때 합치는 방법에 대해 https://seong6496.tistory.com/512 를 참고했고 
마지막 줄은 힌트에서 복붙 했습니다.
'''


if __name__ == "__main__":
    # Demo runs only when executed directly
    def run_demo():
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)         # {'hello':2,'world':1,'ai':1}
        print(f)
        print(top_k(f, 2))               # [('hello',2),('ai',1)] or [('hello',2),('world',1)] (tie by token asc)
        g = merge_freqs([{"x":1},{"x":2,"y":3}])
        print(g)                         # {'x':3,'y':3}
    run_demo()
    pass