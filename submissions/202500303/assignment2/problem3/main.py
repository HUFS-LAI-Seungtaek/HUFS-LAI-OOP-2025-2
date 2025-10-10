# main.py
def count_tokens(tokens: list[str]) -> dict[str, int]:
    if not tokens:
        return {}
    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1 
    return d

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    if k<=0:
        return []
    if k> len(freqs):
        k = len(freqs)
    return sorted(freqs.items(), key=lambda x: (-x[1], x[0]))[:k] # gpt 도움을 받음 
    #key는 sort 정렬 기준, lambda는 임시함수 (count를 음수값으로 하여 내림차순 효과를 받음)

def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
    final_dict = {}
    for freq_dict in maps:
        for key, value in freq_dict.items():
            final_dict[key] = final_dict.get(key, 0) + value
    return final_dict


if __name__ == "__main__":
        tokens = ["hello","world","hello","ai"]
        f = count_tokens(tokens)         # {'hello':2,'world':1,'ai':1}
        print(f)
        print(top_k(f, 2))               # [('hello',2),('ai',1)] or [('hello',2),('world',1)] (tie by token asc)
        g = merge_freqs([{"x":1},{"x":2,"y":3}])
        print(g)                         # {'x':3,'y':3}
        #run_demo()
        #pass
