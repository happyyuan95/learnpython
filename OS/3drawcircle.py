import turtle

#https://blog.csdn.net/sandalphon4869/article/details/99443949

#奥运五环
turtle.pensize(10)  #画笔尺寸
'''
turtle.circle(radius半径, 
extent=None角度, 
steps=None未指定绘制圆弧，指定绘制多边形)
'''

'''
turtle.circle(100)  #画圈，传参为半径

turtle.penup()   #抬起画笔
turtle.goto(-212,0)  #跳转位置
turtle.pendown()   #放下画笔
turtle.color("blue")  #更改颜色
turtle.circle(100)

turtle.penup()
turtle.goto(212,0)
turtle.pendown()
turtle.color("red")
turtle.circle(100)

turtle.penup()
turtle.goto(106,-106)
turtle.pendown()
turtle.color("green")
turtle.circle(100)

turtle.penup()
turtle.goto(-106,-106)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)

turtle.reset()  #清空屏幕并回到原点
'''
#turtle.penup()
turtle.color("red")
turtle.circle(100,360,3)
turtle.goto(0,100)

turtle.done()  #继续执行


