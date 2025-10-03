"""
cachekit 패키지 데모 및 테스트 스크립트
"""

if __name__ == "__main__":
    # 상대경로로 패키지 함수와 클래스 가져오기
    from . import Cache, print_version_info, VERSION
    
    print("=" * 40)
    print("cachekit 패키지 데모")
    print("=" * 40)
    
    # 버전 정보 출력
    print_version_info()
    print()
    
    # 캐시 인스턴스 생성
    print("1. 캐시 인스턴스 생성:")
    cache_instance = Cache()
    print(f"   새 캐시 생성: {cache_instance}")
    print(f"   초기 크기: {len(cache_instance)}")
    print()
    
    # 데이터 저장 테스트
    print("2. 데이터 저장 테스트:")
    cache_instance.put("username", "김철수")
    cache_instance.put("age", 25)
    cache_instance.put("city", "서울")
    print(f"   데이터 3개 저장 후 크기: {len(cache_instance)}")
    print(f"   username: {cache_instance.get('username')}")
    print(f"   age: {cache_instance.get('age')}")
    print()
    
    # 덮어쓰기 테스트
    print("3. 데이터 덮어쓰기 테스트:")
    old_age = cache_instance.get("age")
    cache_instance.put("age", 26)
    new_age = cache_instance.get("age")
    print(f"   나이 업데이트: {old_age} → {new_age}")
    print(f"   캐시 크기 (동일): {len(cache_instance)}")
    print()
    
    # 존재하지 않는 키 조회 테스트
    print("4. 존재하지 않는 키 조회:")
    result = cache_instance.get("hobby", "독서")
    print(f"   존재하지 않는 키 'hobby' 조회: {result}")
    missing = cache_instance.get("phone")
    print(f"   기본값 없이 조회: {missing}")
    print()
    
    # 캐시 초기화 테스트
    print("5. 캐시 초기화 테스트:")
    print(f"   초기화 전 크기: {len(cache_instance)}")
    cache_instance.clear()
    print(f"   초기화 후 크기: {len(cache_instance)}")
    print(f"   초기화 후 상태: {cache_instance}")
    
    print("\n" + "=" * 40)
    print("데모 완료!")
    print("=" * 40)