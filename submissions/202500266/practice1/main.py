import time
from tqdm import tqdm  # tqdm 라이브러리를 가져옵니다.

class Country:
    def __init__(self, name: str, gold=0, silver=0, bronze=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        """객체를 출력할 때 표시될 형식을 지정합니다."""
        return f"{self.name}: G{self.gold} S{self.silver} B{self.bronze}"

    # Arithmetic overriding → 메달 합산
    def __add__(self, other):
        """ '+' 연산자를 사용했을 때의 동작을 정의합니다. """
       
        if isinstance(other, Country):
            return Country(
                self.name,
                self.gold + other.gold,
                self.silver + other.silver,
                self.bronze + other.bronze,
            )
        
        

    # Comparison overriding → 금 > 은 > 동 순서로 비교
    def __lt__(self, other: "Country") -> bool:
        """ '<' 연산자를 사용했을 때의 동작을 정의합니다. sorted() 함수가 사용합니다. """
        
        if isinstance(other, Country):
            return (self.gold, self.silver, self.bronze) < (other.gold, other.silver, other.bronze)
        

    def __eq__(self, other: object) -> bool:
        self.gold == other.gold and \
        self.silver == other.silver and \
        self.bronze == other.bronze


if __name__ == "__main__":
    # 샘플 이벤트: (국가, 메달종류)
    events = [
        ("KOR", "gold"), 
        ("KOR", "silver"),
        ("USA", "gold"), 
        ("USA", "gold"), 
        ("USA", "bronze"),
        ("JPN", "gold"), 
        ("JPN", "silver"),
        ("CHN", "bronze"), 
        ("CHN", "bronze"),
    ]

    countries = {}

    
    print("Processing events...")
    for country, medal in tqdm(events, desc="집계 중"):
        time.sleep(0.1)  # 진행바 확인용 딜레이
        if country not in countries:
            countries[country] = Country(country)
        
        if medal == "gold":
            countries[country].gold += 1
        elif medal == "silver":
            countries[country].silver += 1
        elif medal == "bronze":
            countries[country].bronze += 1

    # 리더보드 출력 (금→은→동 기준 내림차순)
    # __lt__에 정의된 비교 기준에 따라 정렬됩니다.
    # reverse=True 이므로 메달이 많은 순서(내림차순)로 정렬됩니다.
    leaderboard = sorted(countries.values(), reverse=True)

    print("\n=== Medal Leaderboard ===")
    for rank, c in enumerate(leaderboard, start=1):
        print(f"{rank:>2}. {c}")