
# 아이템 부모 클래스

class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    
    def discard(self):
        if self.isdropable == True:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")

# 장비 아이템 자식 클래스
class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        print(f"{self.name} 착용 완료 : {sword.effect}")

# 소모 아이템 자식 클래스
class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def use(self):
        print(f"{self.name} 사용 완료 : {elixir.effect}")


# 인스턴스 생성

sword = WearableItem("커다란 검", 500, 40, False, "공격력 350 증가")
sword.wear()
sword.sale()
sword.discard()

print("")

elixir = UsableItem("엘릭서", 1500, 20, True, "체력 5000 회복")
elixir.use()
elixir.sale()
elixir.discard()