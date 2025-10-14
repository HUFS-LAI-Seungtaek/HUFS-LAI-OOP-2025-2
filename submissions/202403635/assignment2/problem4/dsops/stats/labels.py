# 생성형 AI Gemini 사용범위: 코드 초안 생성, 파이썬 특정 기능과 코드 제안 및 설명 (코드 제안 시 같은 줄에 명시), 작성한 코드 리뷰 요청

def label_distribution(labels: list[str]) -> dict[str, int]:

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1 # 해당 코드를 생성형 AI Gemini에게 제안받았습니다.
    return counts
