# 원화와 환율을 입력 -> 달러값 출력

won = input("원화 금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요 >>> ")

try: # 예외가 발생할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as error: # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다.", error)
except ZeroDivisionError as error:
    print("0으로 나누는 것은 불가능합니다.", error)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드입니다.")
finally: # 파일을 닫아주는 용도
    print("항상 실행되는 코드입니다.")

print("프로그램이 끝났나요?")