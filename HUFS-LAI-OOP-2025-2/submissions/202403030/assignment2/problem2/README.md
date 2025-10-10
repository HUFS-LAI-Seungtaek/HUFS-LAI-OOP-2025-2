# Problem 2 - textops (clean & tokenize; root re-export, __all__, relative imports)

## Files
다음 파일들을 만들어서 같은 최상위 폴더에 배치하세요(패키지 구조):

```
textops/
  __init__.py          # 루트 API 재노출(re-export) + __all__
  main.py              # 데모 실행
  clean/
    __init__.py
    filters.py         # clean_text(s)
  tokenize/
    __init__.py
    word.py            # word_tokens(s)
```

## Goal
간단한 AI/NLP 전처리 패키지 만들기. 텍스트 정규화(`clean_text`) 후 단일 공백 기반 토큰화(`word_tokens`).
사용자는 루트에서 바로 사용:

```python
from textops import clean_text, word_tokens
```

## Why this package exists (동작 원리 & 존재 이유)
- 동작 원리: `clean_text`가 문자열을 표준화 (소문자화 → 앞뒤 공백 제거 → 모든 공백 압축 → 특정 문장부호 제거). `word_tokens`는 이미 정규화된 문자열을 단일 공백으로 분리.
- 존재 이유: 전처리 → 토큰화는 모든 NLP 파이프라인의 기본 빌딩 블록. 패키지 루트에서 API를 노출하면 사용성이 좋아지고 import 경로가 단순해짐.

## Required API
- `clean_text(s: str) -> str` (`clean/filters.py`)
  - 규칙:
    - 전부 소문자
    - 앞뒤 공백 제거
    - 모든 연속 공백(스페이스/탭/개행 등)을 한 칸으로 축약
    - ASCII 문장부호 제거 (단, `'`(apostrophe)과 `-`(hyphen)은 유지)

- `word_tokens(s: str) -> list[str]` (`tokenize/word.py`)
  - 규칙:
    - 단일 공백 기준 분할
    - 빈 문자열/공백뿐이면 `[]` 반환

- 루트(`textops/__init__.py`)에서 재노출 + `__all__ = ["clean_text", "word_tokens"]`
- 내부에서 상대경로 import 사용

## Rules
- 라이브러리 함수 내 print/I/O 금지(순수 함수).
- 전역 가변 상태 금지.
- 예외는 간단 명료한 메시지.

## Examples
```python
from textops import clean_text, word_tokens
s = "  Hello,   WORLD!  "
clean_text(s)                 # "hello world"
word_tokens("hello world")    # ["hello", "world"]
```

## Edge cases (반드시 처리)
- `"\tHello,\nWORLD!!! "` → `"hello world"`
- `"..."` → `""` (모두 제거)
- `"ROCK-'N'-ROLL!!"` → `"rock-'n'-roll"` (`'`, `-` 유지)

## Instructor quick test
```python
from textops import clean_text, word_tokens
print(clean_text(" \tHello,\nWORLD!!!  "))  # "hello world"
print(word_tokens("hello world"))           # ["hello", "world"]
```