from tqdm import tqdm

class Country:
    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        # 디버깅에 유용한 포맷
        return f"Country('{self.name}', {self.gold}, {self.silver}, {self.bronze})"
    
    # Task 1: __add__ 구현
    def __add__(self, other):
        if self.name != other.name:
            # 과제 요구사항에 따라 이름을 유지하거나 에러 처리 필요
            pass 
        
        new_gold = self.gold + other.gold
        new_silver = self.silver + other.silver
        new_bronze = self.bronze + other.bronze
        return Country(self.name, new_gold, new_silver, new_bronze)

    # Task 2: __lt__ (Less Than, 작다) 구현 - 정렬 기준 (금 > 은 > 동 순서)
    def __lt__(self, other):
        # 금메달이 적으면 작다 (순위 낮음)
        if self.gold != other.gold:
            return self.gold < other.gold 
        
        # 은메달이 적으면 작다
        if self.silver != other.silver:
            return self.silver < other.silver
        
        # 동메달이 적으면 작다 (sorted(reverse=True)를 위해)
        if self.bronze != other.bronze:
            return self.bronze < other.bronze
            
        return False

    # Task 3: __eq__ (Equal, 같다) 구현
    def __eq__(self, other):
        return (self.gold == other.gold and
                self.silver == other.silver and
                self.bronze == other.bronze)

# --- 메인 실행 함수 ---
def run_leaderboard_practice():
    # 과제 예시 결과를 재현하는 이벤트 리스트 (USA: G2 S0 B1, KOR: G1 S1 B0 등)
    events = [
        ("USA", "G"), ("USA", "G"), ("USA", "B"), # USA: G2 B1
        ("KOR", "G"), ("KOR", "S"), # KOR: G1 S1
        ("JPN", "G"), ("JPN", "S"), # JPN: G1 S1
        ("CHN", "B"), ("CHN", "B"), # CHN: B2
    ]

    # 순위표 초기화
    leaderboard = {}

    # Task 4: tqdm을 사용한 진행률 추적 및 메달 업데이트
    for country_name, medal_type in tqdm(events, desc="Processing events"):
        if country_name not in leaderboard:
            leaderboard[country_name] = Country(country_name, 0, 0, 0)
        
        # 새로운 메달 객체 생성 (1, 0, 0 또는 0, 1, 0 등)
        new_medal = Country(country_name, 0, 0, 0)
        if medal_type == "G": new_medal.gold = 1
        elif medal_type == "S": new_medal.silver = 1
        elif medal_type == "B": new_medal.bronze = 1

        # __add__ 메소드를 사용하여 메달 합산 (Task 1 활용)
        leaderboard[country_name] = leaderboard[country_name] + new_medal

    # 순위표 출력
    print("\n=== Medal Leaderboard ===")

    # Task 2의 __lt__ 메소드를 사용하여 정렬 (높은 순위가 위로 오도록 reverse=True)
    sorted_countries = sorted(leaderboard.values(), reverse=True)

    for i, country in enumerate(sorted_countries, 1):
        # 과제 요구 포맷: G# S# B#
        print(f"{i}. {country.name}: G{country.gold} S{country.silver} B{country.bronze}")

# 프로그램의 메인 진입점에서 run_leaderboard_practice 함수 실행
if __name__ == "__main__":
    # 테스트 코드에 의해 무시되지 않도록 직접 실행
    run_leaderboard_practice()
