# 상속
# - 클래스들의 중복된 코드를 제거하고 유지보수를
#   편하게 하기 위해서 사용

# 클래스 변수
# - 인스턴스들이 모두 공유하는 변수 (max_num)

import random

# 부모 클래스

class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
        
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shack(Monster):
    def move(self): # 메서드 오버라이딩 (move 함수 재정의)
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        # 부모클래스의 __init__ 을 불러옴

        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] 날아오르기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")

# 인스턴스
wolf = Wolf("늑대", 1500, 200) # Monster Class 의 init
wolf.move() # Monster Class 의 move
print(wolf.max_num)

shark = Shack("상어", 3000, 400) # Monster Class 의 init
shark.move() # shark 메서드 오버라이딩 재정의
print(shark.max_num)

dragon = Dragon("드래곤", 8000, 800) # Monster Class 의 init
dragon.move() # dragon 메서드 오버라이딩 재정의
dragon.skill()
print(dragon.max_num)