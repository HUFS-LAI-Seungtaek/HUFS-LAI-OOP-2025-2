# main.py
def count_tokens(tokens: list[str]) -> dict[str, int]:
    d = {}
    for token in tokens:
        d[token] = d.get(token, 0) + 1
    return d

def top_k(freqs: dict[str, int], k: int) -> list[tuple[str, int]]:
    return sorted(freqs.items(), key=lambda x: (-x[1], x[0]))[:k]


def merge_freqs(maps: list[dict[str, int]]) -> dict[str, int]:
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
    run_demo()
    pass