from tqdm import tqdm

class Country:
    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __repr__(self):
        return f"Country('{self.name}', {self.gold}, {self.silver}, {self.bronze})"
    
    def __add__(self, other):
        if self.name != other.name:
            pass 
        
        new_gold = self.gold + other.gold
        new_silver = self.silver + other.silver
        new_bronze = self.bronze + other.bronze
        return Country(self.name, new_gold, new_silver, new_bronze)

    def __lt__(self, other):
        if self.gold != other.gold:
            return self.gold < other.gold 
        
        if self.silver != other.silver:
            return self.silver < other.silver
        
        if self.bronze != other.bronze:
            return self.bronze < other.bronze
            
        return False

    
    def __eq__(self, other):
        return (self.gold == other.gold and
                self.silver == other.silver and
                self.bronze == other.bronze)

def run_leaderboard_practice():
    events = [
        ("USA", "G"), ("USA", "G"), ("USA", "B"), # USA: G2 B1
        ("KOR", "G"), ("KOR", "S"), # KOR: G1 S1
        ("JPN", "G"), ("JPN", "S"), # JPN: G1 S1
        ("CHN", "B"), ("CHN", "B"), # CHN: B2
    ]

    leaderboard = {}

    # tqdm을 사용한 메달수 업데이트 부분 제미나이 도움 받음
    for country_name, medal_type in tqdm(events, desc="Processing events"):
        if country_name not in leaderboard:
            leaderboard[country_name] = Country(country_name, 0, 0, 0)
        
        new_medal = Country(country_name, 0, 0, 0)
        if medal_type == "G": new_medal.gold = 1
        elif medal_type == "S": new_medal.silver = 1
        elif medal_type == "B": new_medal.bronze = 1

        leaderboard[country_name] = leaderboard[country_name] + new_medal

    print("\n=== Medal Leaderboard ===")

    sorted_countries = sorted(leaderboard.values(), reverse=True)

    for i, country in enumerate(sorted_countries, 1):
        print(f"{i}. {country.name}: G{country.gold} S{country.silver} B{country.bronze}")

if __name__ == "__main__":
    run_leaderboard_practice()
