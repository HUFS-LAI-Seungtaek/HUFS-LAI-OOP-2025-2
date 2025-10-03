def word_tokens(s: str) -> list[str]:
    s = s.strip()
    if not s:
        return []
    return s.split(' ')
