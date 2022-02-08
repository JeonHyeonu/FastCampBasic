origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 : ")

if input_pass == origin_pass:
    print("로그인 완료.")
    print("반갑습니다.")
elif input_pass == "":
    print("입력한 문자가 없습니다.")
    print("다시 입력해주세요.")
else:
    print("로그인 실패.")
    print("잘못된 비밀번호입니다. 다시 입력해주세요.")