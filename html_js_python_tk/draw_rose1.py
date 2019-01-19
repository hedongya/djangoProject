## Created on Nov 18, 2017 @author: QiZhao
# -*- coding: cp936 -*-
import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("draw a rose")

tt = turtle.Turtle()
# 设置初始位置
tt.penup()
tt.left(90)
tt.fd(200)
tt.pendown()
tt.right(90)

# 花蕊
tt.fillcolor("red")
tt.begin_fill()
tt.circle(10,180)
tt.circle(25,110)
tt.left(50)
tt.circle(60,45)
tt.circle(20,170)
tt.right(24)
tt.fd(30)
tt.left(10)
tt.circle(30,110)
tt.fd(20)
tt.left(40)
tt.circle(90,70)
tt.circle(30,150)
tt.right(30)
tt.fd(15)
tt.circle(80,90)
tt.left(15)
tt.fd(45)
tt.right(165)
tt.fd(20)
tt.left(155)
tt.circle(150,80)
tt.left(50)
tt.circle(150,90)
tt.end_fill()
 
# 花瓣1
tt.left(150)
tt.circle(-90,70)
tt.left(20)
tt.circle(75,105)
tt.setheading(60)
tt.circle(80,98)
tt.circle(-90,40)

# 花瓣2
tt.left(180)
tt.circle(90,40)
tt.circle(-80,98)
tt.setheading(-83)

# 叶子1
tt.fd(30)
tt.left(90)
tt.fd(25)
tt.left(45)
tt.fillcolor("green")
tt.begin_fill()
tt.circle(-80,90)
tt.right(90)
tt.circle(-80,90)
tt.end_fill()
 
tt.right(135)
tt.fd(60)
tt.left(180)
tt.fd(85)
tt.left(90)
tt.fd(80)
 
# 叶子2
tt.right(90)
tt.right(45)
tt.fillcolor("green")
tt.begin_fill()
tt.circle(80,90)
tt.left(90)
tt.circle(80,90)
tt.end_fill()
 
tt.left(135)
tt.fd(60)
tt.left(180)
tt.fd(60)
tt.right(90)
tt.circle(200,60)
tt.ht() # hideturtle
window.exitonclick()
