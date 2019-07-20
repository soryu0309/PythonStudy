# -*- coding:utf-8

import turtle as t

#삼각형 그리기

t.color("red") #펜 색을 빨강으로 바꾼다.
t.pensize(3) #펜 사이즈를 3으로 바꾼다.
t.forward(100) #거북이가 앞으로 100 이동한다.
t.left(120) #거북이가 왼쪽으로 120도 회전한다.
#이 같은 과정을 3번 반복 한다.
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

#사각형 그리기

t.color("green") #펜 색을 초록으로 바꾼다.
t.pensize(5) #펜 사이즈를 5로 바꾼다.
t.forward(100) #거북이가 앞으로 100 이동한다.
t.left(90) #거북이가 왼쪽으로 90도 회전한다.
# 이 같은 과정을 4번 반복 한다.
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

#원 그리기

t.color("blue") #펜 색을 파랑으로 바꾼다.
t.pensize(7) #펜 사이즈를 7로 바꾼다.
t.circle(50) # 반지름 50 짜리 원을 그린다.
