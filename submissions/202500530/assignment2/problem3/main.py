# main.py
"""
Problem 3 — tokenstats (module + __main__ demo)
- count token frequencies
- get top-k (freq desc, token asc for ties)
"""
#gpt
# token을 순회할 때 unhashable error가 발생하여 이에 대한 정보를 물었습니다.
# key 빈도와 token을 동시에 정렬하는 과정에서 진행이 불가하여 도움을 받았습니다.
# dict를 순회 및 여러 계산을 할 때 필요한 코드와 items()가 무슨 역할을 하는지 물어보았습니다.

def count_tokens(tokens: list[str]) -> dict[str, int]:

    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1
    return d
    
    
def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:

    if k <= 0 :
        return []
    result = sorted(freqs.items(), key=lambda x: (-x[1], x[0])) #
    
    return result[:k]


    


def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for freq_dict in maps:
        for key, value in freq_dict.items():
            result[key] = result.get(key,0) + value
    return result



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