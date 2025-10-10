
def label_distribution(labels:list[str])-> dict[str, int]:
    freqs = {}
    for label in labels:
        freqs[label] = freqs.get(label,0)+1
    return freqs
#problem3 count_tokens 함수 참고하였습니다
