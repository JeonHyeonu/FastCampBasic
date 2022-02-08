# x = int(input("몇 단을 출력할까요? "))

# for i in range(1, 10):
#     print("{} * {} = {}".format(x, i, x*i))




# print("[메뉴를 입력하세요]")
# 1. 게임시작 2. 랭킹보기 3. 게임종료

# while True:
#     print("[메뉴를 입력하세요]")
#     x = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))
#     if x == 1:
#         print("게임을 시작합니다")
#     elif x == 2:
#         print("실시간 랭킹")
#     elif x == 3:
#         print("게임종료")
#         break
#     else:
#         print("다시 입력해 주세요")

# print("Let's Learning Korean")

# word_list = ["사랑해", "행복해", "고마워"]

# for i in word_list:
#     print(i)
#     x = input()

#     if i == x:
#         continue
#     elif i != x:
#         break

print("Let's Learning Korean")

word_list = ["사랑해", "행복해", "고마워", "최고야"]

count = 0

for i in word_list:
    print(i)
    x = input()

    if i == x:
        count += 1
    else:
        break

print("전체 문제 갯수 : ", len(word_list))
print("맞춘 문제 갯수 : ", count)
print("틀린 문제 갯수 : ", len(word_list) - count)