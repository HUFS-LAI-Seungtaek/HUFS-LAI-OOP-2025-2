from cachekit import Cache, print_version_info, VERSION
if __name__ == "__main__":
    print("--- cachekit Demo ---")
    print_version_info()
    print(f"VERSION variable is: {VERSION}")
    print("\nCreating and using Cache object...")
    c = Cache()
    c.put("a", 1)
    c.put("b", "hello")
    print(f"After putting 'a' and 'b': len(c) = {len(c)}")
    print(f"Getting 'a': {c.get('a')}")
    c.put("a", 999)
    print(f"After overwriting 'a': {c.get('a')}")
    print(f"Getting missing key 'c' with default 42: {c.get('c', 42)}")
    c.clear()
    print(f"After clearing the cache: len(c) = {len(c)}")
    print("\n--- Demo Finished ---")
"""
(도움받은 내용):
cachekit 패키지의 Cache 클래스를 구현하며 생성형 AI(Gemini)의 도움을 받았습니다. 파이썬 딕셔너리를 활용한 클래스 래핑 방법과, __len__과 같은 특별 메서드의 역할에 대해 학습했습니다.
"""