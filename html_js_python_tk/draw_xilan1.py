# -*- coding: cp936 -*-
# http://blog.csdn.net/qq_38300153/article/details/71056511
# Turtle 绘制一棵西兰花
# 绘制一棵西兰花，从主干出发以一定的角度向左向右生成对称的枝干，
# 再从每个枝干出发向左向右生成对称的枝干，循环此动作，
# 并最终绘制出一棵漂亮的西兰花。
import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title(u"draw 西兰花")

def tree(plist,l,a,f):
    if l>5:
        lst=[]
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)

def maketree(x,y,clr):
    p = turtle.Turtle()
    p.pensize(5)
    p.color(clr)
    p.hideturtle()
    p.getscreen().tracer(30,0)
    #p.speed(10)
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()
    t=tree([p],200,20,0.6375)
    #print(len(p.getscreen().turtles()))

def main():
    maketree(0,-300,"green")

main()
window.exitonclick()
