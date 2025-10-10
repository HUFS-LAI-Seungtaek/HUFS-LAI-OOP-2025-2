from tqdm import tqdm
import time

class Country:
    def __init__(self, name: str, gold=0, silver=0, bronze=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        return f"{self.name}: G{self.gold} S{self.silver} B{self.bronze}"

    # Arithmetic overriding → 메달 합산
    def __add__(self, other):
        return self.gold + other.gold, self.silver + other.silver, self.bronze + other.bronze

    # Comparison overriding → 금 > 은 > 동 순서로 비교
    def __lt__(self, other: "Country") -> bool:
        if self.gold != other.gold:
            return self.gold < other.gold
        elif self.silver != other.silver:
            return self.silver < other.silver
        else:
            return self.bronze < other.bronze

    def __eq__(self, other: object) -> bool:
        return self.name == other.name, self.gold == other.gold and self.silver == other.silver and self.bronze == other.bronze


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

    # TODO: tqdm으로 집계 진행
    for country, medal in tqdm(events, desc="Processing events"):
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
    leaderboard = sorted(countries.values(), reverse=True)

    print("\n=== Medal Leaderboard ===")
    for rank, c in enumerate(leaderboard, start=1):
        print(f"{rank:>2}. {c}")