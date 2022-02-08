# 튜플 >>> 읽기 전용 리스트
# - 수정, 추가, 삭제가 불가능한 "리스트"
# - 메모리 사용이 효율적
# - "읽기전용" 이기 때문에 데이터 손실 걱정 X

a = 10, 20, 30, 40, 50 # 또는 (10, 20, 30, 40, 50)

print(a.index(20)) # 특정값의 인덱스
print(a.count(30)) # 특정값의 갯수
print(max(a), min(a)) # 최대값, 최소값
print(sum(a))


# 패킹
numbers = 3, 4, 5

# 언패킹
x, y, z = numbers

print(x)
print(y)
print(z)