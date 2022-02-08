import random

def getRandomNumber():
    number = random.randint(1, 45)
    return number


num_list = [] # 로또 번호 저장할 리스트



while True:
    random_num = getRandomNumber()
   
    if random_num not in num_list:
        num_list.append(random_num)
        if len(num_list) == 6:
            break
        else:
            continue

# 중복되는 번호가 몇번 나올지 예상이 안되기 때문에 for 문은 적절치 않음
# for i in range(6):
#     random_num = getRandomNumber()

#     if random_num not in num_list:
#         num_list.append(random_num)

num_list.sort()

print(num_list)



for i in num_list:
    print(i, end=" ")