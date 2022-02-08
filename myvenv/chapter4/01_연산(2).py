# 1. 비교 연산
print("---비교연산---")
print(2 > 3) # False
print(15 < 30) # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("가나다" == "가나라") # False
print("111111111" != "1111111111") # True

# 2. 논리 연산
print("---논리연산---")
print(4 < 6 and 10 >= 10) # True and True -> True
print("포기하지마" != "포기하지마" or "나는할수있다" == "나는할수있다") #False or True -> True
print(not 5==5) # not True -> False

# 3. 멤버십 연산
print("---멤버십 연산---")
print("a" in "abc") # abc 안에 a가 포함되어 있다면 True -> True
print("d" in "abc") # abc 안에 d가 포함되어 있다면 True -> False
print("f" not in "abc") # abc 안에 f가 포함되어 있지 않다면 True -> True
print("c" not in "abc") # abc 안에 c가 포함되어 있지 않다면 True -> False

