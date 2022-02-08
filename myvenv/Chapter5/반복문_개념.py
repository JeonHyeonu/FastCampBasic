# 반복문
# - 반복해서 명령을 사용하고 싶을 때

# 시퀀스 자료형
# - 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리




# for 문
# - 리스트 자료형 사용

exercise = ["축구", "야구", "농구"]

for i in exercise:
    print("선택한 종목은 {} 입니다.".format(i))



# - 문자열 사용

fighting_message = "자신감을 가지자! 나에게 한계란 없다!"

for word in fighting_message:
    print(word) # 문자 한글자씩 세로로 출력되는 결과



# range 객체 사용
# - range(10) -> 0~9까지의 숫자를 포함하는 range 객체 0,1,2,3,4,5,6,7,8,9
# - range(시작, 끝+1, 간격)

for i in range(1, 10):
    print(i,end=" ")

print("")

for i in range(1, 10, 3):
    print(i,end=" ")