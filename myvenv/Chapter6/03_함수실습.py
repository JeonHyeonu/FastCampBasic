

def printSumAvg(x,y,z):
    # docstring : 설명문 ↓
    """
    두 수의 합계와 평균을 출력하는 함수 \n
    매개변수에 대한 설명을 적어놓을수 있기 때문에 코딩 작성시 참고하기 좋음
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum}")
    print(f"평균 : {int(avg)}")

printSumAvg(10, 20, 30)