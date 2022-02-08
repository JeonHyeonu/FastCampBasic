# study_time = input("공부한 시간을 입력하세요 : ")

# if int(study_time) >= 10:
#     print("잠금이 해제됐습니다")
# elif int(study_time) >= 5:
#     print("30분 사용 가능")
# else:
#     print("사용이 불가능합니다")


# price_now = int(input("현재 가진 금액 : "))

# if price_now >= 20000:
#     print("오늘 저녁은 치킨")
# elif price_now >= 10000:
#     print("오늘 저녁은 떡볶이")
# elif price_now >= 2000:
#     print("오늘 저녁은 김밥")

korean = int(input("국어 : "))
math = int(input("수학 : "))
eng = int(input("영어 : "))

total = korean + math + eng
avg = total / 3

if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력했습니다.")