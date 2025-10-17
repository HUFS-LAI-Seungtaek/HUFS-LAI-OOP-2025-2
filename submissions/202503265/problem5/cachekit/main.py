from cachekit import Cache, print_version_info

def run_demo():
    """패키지 기능 시연 함수"""
    print("--- cachekit 데모 시작 ---")
    
    print_version_info()

    c = Cache()
    print(f"\n빈 캐시 생성됨, 현재 길이: {len(c)}")

    c.put("user_id", 123)
    c.put("username", "gemini")
    print(f"데이터 2개 추가 후 길이: {len(c)}")

    print(f"username 조회: {c.get('username')}")
    
    print(f"없는 'email' 키 조회 (기본값): {c.get('email')}")
    print(f"없는 'email' 키 조회 (사용자 정의 기본값): {c.get('email', 'N/A')}")

    c.put("username", "gemini-pro")
    print(f"username 덮어쓴 후 조회: {c.get('username')}")
    print(f"덮어쓴 후 길이 (변화 없음): {len(c)}")

    c.clear()
    print(f"캐시 clear 후 길이: {len(c)}")
    print("--- cachekit 데모 종료 ---")


if __name__ == "__main__":
    run_demo()