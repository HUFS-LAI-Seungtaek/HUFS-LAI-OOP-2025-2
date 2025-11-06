
if __name__ == "__main__":
    from . import Cache, print_version_info, VERSION

    print("--- cachekit 데모 ---")
    print_version_info()
    print(f"현재 버전: {VERSION}")

    # Cache 인스턴스 생성 및 사용
    c = Cache()
    print(f"\n빈 캐시 생성됨. 현재 길이: {len(c)}")

    print('c.put("a", 1) 실행...')
    c.put("a", 1)
    print(f"키 'a'로 1을 저장함. 현재 길이: {len(c)}")
    print(f"c.get('a') 결과: {c.get('a')}")

    print("\n동일한 키 'a'에 999를 덮어쓰기...")
    c.put("a", 999)
    print(f"c.get('a') 결과: {c.get('a')}")

    print(f"\n존재하지 않는 키 'missing' 조회 (기본값 42): {c.get('missing', 42)}")

    print("\nc.clear() 실행...")
    c.clear()
    print(f"캐시 비워짐. 현재 길이: {len(c)}")
