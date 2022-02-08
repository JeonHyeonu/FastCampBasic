# 클래스
# - 객체를 만들기 위한 설계도
# 예) 제과제빵 시트, 또는 틀

# 객체
# - 설계도로부터 만들어낸 제품
# 예) 시트나 틀으로 만들어낸 빵

# 클래스를 사용하는 이유

print("========클래스를 사용하지 않았을 때========")

champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name} 님, 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name} 님, 소환사의 협곡에 오신것을 환영합니다.")

champion3_name = "야스오"
champion3_health = 700
champion3_attack = 88

print(f"{champion2_name} 님, 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

print("")

print("========클래스를 사용했을 때========")

class Champions:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name} 님, 소환사의 협곡에 오신것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")

ezreal = Champions("이즈리얼", 700, 90)
leesin = Champions("리신", 800, 95)
yasuo = Champions("야스오", 700, 88)

ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()