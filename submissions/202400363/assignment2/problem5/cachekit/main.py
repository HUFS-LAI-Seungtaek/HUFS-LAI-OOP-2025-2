# cachekit/main.py

if __name__ == "__main__":
    from . import Cache, print_version_info, VERSION
    
    print("--- cachekit 데모 시작 ---")
    
    # 1. 버전 정보 출력
    print_version_info()
    print(f"패키지 버전: {VERSION}")
    
    # 2. 캐시 객체 생성 및 사용
    cache = Cache()
    print(f"초기 캐시 크기: {len(cache)}")
    
    # put과 get 메서드 테스트
    cache.put("user_id", 123)
    cache.put("data", [1, 2, 3])
    
    print(f"'user_id' 값: {cache.get('user_id')}")
    print(f"현재 캐시 크기: {len(cache)}")
    
    # 존재하지 않는 키 테스트
    print(f"없는 키 조회 (기본값): {cache.get('non_existent_key', 'not_found')}")
    
    # 3. clear 메서드 테스트
    cache.clear()
    print(f"clear 후 캐시 크기: {len(cache)}")
    
    print("--- 데모 완료 ---")
    