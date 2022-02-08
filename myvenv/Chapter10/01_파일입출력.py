# 1. 파일 쓰기
file = open("./myvenv/Chapter10/data.txt", "w", encoding="utf8")
# 경로를 지정하지 않으면 기본 root 폴더에 저장
file.write("1. 스타트코딩과 함께 파이썬 공부")
file.close()



# 2. 파일 추가
file = open("./myvenv/Chapter10/data.txt", "a", encoding="utf8")
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()



# # 3. 파일 읽기
# file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")

# # 3-1 파일 전체 읽기
# data = file.read()
# print(data)
# file.close()

# # 3-2 파일 한 줄 읽기
# while True:
#     data = file.readline()
#     print(data, end="")
#     if data == "":
#         break
# file.close()



# # 번외 >> with 구문
# # - 미사용
# file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")
# data = file.read()
# file.close()

# 사용 (file.close() 구문 생략 가능)
with open("./myvenv/Chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)