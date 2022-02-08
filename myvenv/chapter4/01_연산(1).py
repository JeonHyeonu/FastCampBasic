# 대입 연산
# 변수 이름 = 데이터
month = 1
print("이번달: {}월".format(month))

# 산술 연산
# - 숫자 연산
x = 5
y = 2

print(x + y) # 더하기
print(x - y) # 빼기
print(x * y) # 곱하기
print(x / y) # 나누기
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱


# - 문자열 연산
tag_1 = "#C++ "
tag_2 = "#JAVA "
tag_3 = "#PYTHON"

tag = tag_1 + tag_2 + tag_3

print(tag)

msg = "웹코딩을 꾸준히 하자! \n" * 5
print(msg)


# 복합 할당 연산자
price = 20000 # 가격 10% 인상
price += 2000 # price = price + 2000

weight = 80 # 무게 1.5배 감소
weight /= 1.5 # weight = weight / 1.5
weight = round(weight, 2)


size = 160 # 사이즈 줄어듬
size -= 10 # size = size - 10

volume = 10000 # 배터리 용량 1.5배 증가
volume *= 1.5 # volume = volume * 1.5

print(price, weight, size, volume)