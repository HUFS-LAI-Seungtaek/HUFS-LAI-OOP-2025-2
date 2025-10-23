# cachekit/main.py

# 상대 경로 임포트로 __init__.py에서 노출된 API를 사용
from . import Cache, print_version_info, VERSION

def run_demo():
    print("--- Problem 5 cachekit Demo ---")
    
    # 1. 버전 정보 출력
    print_version_info()
    
    # 2. Cache 인스턴스 생성 및 테스트
    c = Cache()
    print(f"Initial length: {len(c)}") # 0
    
    # 3. 데이터 저장 및 조회
    c.put("user_id", 101)
    c.put("data_key", [1, 2, 3])
    
    print(f"Length after put: {len(c)}") # 2
    print(f"Get 'user_id': {c.get('user_id')}") # 101
    
    # 4. 동일 키 덮어쓰기 및 조회
    c.put("user_id", 999) 
    print(f"Get 'user_id' after overwrite: {c.get('user_id')}") # 999
    
    # 5. Edge Case: 누락된 키 조회
    print(f"Get missing key (default=42): {c.get('missing_key', 42)}") # 42
    
    # 6. 초기화
    c.clear()
    print(f"Length after clear: {len(c)}") # 0

if __name__ == "__main__":
    # Instructor quick test 포함 (데모 실행)
    print_version_info()
    c = Cache(); c.put("a", 1); print(len(c), c.get("a"))
    c.put("a", 999); print(c.get("a"))                    
    c.clear(); print(len(c))                              
    print(c.get("missing", 42))