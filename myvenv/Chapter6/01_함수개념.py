# 함수를 사용하는 이유

# 함수를 사용하지 않은 경우

print("안녕하세요. XXX 님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. YYY 님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. ZZZ 님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")


# 함수를 사용한 경우

def Guide_Message(name, date):
    print("안녕하세요. {} 님".format(name))
    print("현재 프리미엄 서비스 사용기간이 {}일 남았습니다.".format(date))

Guide_Message("KKK", 50)