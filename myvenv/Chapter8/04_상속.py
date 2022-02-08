# 상속
# - 클래스들의 중복된 코드를 제거하고 유지보수를
#   편하게 하기 위해서 사용

# 부모 클래스

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shack(Monster):
    def move(self): # 메서드 오버라이딩 (move 함수 재정의)
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날아오르기")

# 인스턴스
wolf = Wolf("늑대", 1500, 200) # Monster Class 의 init
wolf.move() # Monster Class 의 move

shark = Shack("상어", 3000, 400) # Monster Class 의 init
shark.move() # shark 메서드 오버라이딩 재정의

dragon = Dragon("드래곤", 8000, 800) # Monster Class 의 init
dragon.move() # dragon 메서드 오버라이딩 재정의