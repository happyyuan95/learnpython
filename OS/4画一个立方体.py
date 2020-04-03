import turtle

#画第一个正方形
turtle.goto(0,200)
turtle.goto(200,200)
turtle.goto(200,0)
turtle.goto(0,0)

#画第二个正方形
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.goto(100,-100)

#将两个正方形连接起来
turtle.goto(200,0)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(200,200)
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.goto(-100,100)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.goto(0,0)
turtle.done()  #继续执行