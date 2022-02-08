# 내장 모듈
# - 파이썬 설치 시 자동으로 설치되는 모듈 (예 : random)

import math

print(math.pi)
print(math.ceil(13.55))

# from math import pi, ceil as c
# print(pi)
# print(c(13.55))



# 외부 모듈
# - 다른 사람이 만든 파이썬 파일을 pip 로 설치 후 사용
# pyautogui

import pyautogui as pg

pg.moveTo(500, 500, duration=2) # 가로세로 500 위치로 마우스 커서를 2초간 이동

