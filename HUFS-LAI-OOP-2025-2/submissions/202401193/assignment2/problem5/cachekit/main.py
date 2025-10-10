# cachekit/main.py

if __name__ == "__main__":
    # 루트 API에서 필요한 클래스와 함수를 상대 경로로 임포트
    from . import Cache, print_version_info
    
    print_version_info()
    
    # 캐시 생성 및 테스트
    c = Cache()
    c.put("a", 1)
    
    print(len(c), c.get("a"))
    
    # 덮어쓰기 및 missing key 테스트
    c.put("a", 999)
    print(c.get("a"))
    print(c.get("missing", 42))

    # clear 및 길이 테스트
    c.clear() 
    print(len(c))
    
    print("\nAll cachekit demos complete.")
