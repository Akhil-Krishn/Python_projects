import turtle
rect_l = 500
rect_b = 150
turtle.Screen()
turtle.speed(10)
turtle.penup()
turtle.goto(-rect_l/2,rect_b/2)
turtle.pendown()
for i in range(0,3): 
    turtle.goto(-rect_l/2,(i*-rect_b)+(rect_b/2))
    hor = False
    if i == 0:
        turtle.fillcolor("#F4C430")
    elif i == 1:
        turtle.fillcolor("white")
    else:
        turtle.fillcolor("#008000")
    turtle.begin_fill()
    for j in range(4):
        if hor:
            turtle.left(90)
            turtle.forward(rect_b)
            turtle.left(90)
            hor = False
        else:
            turtle.forward(rect_l)
            hor = True
    else:
        turtle.end_fill()
turtle.penup()
turtle.goto(-55,-15)
turtle.pendown()
turtle.pencolor("#4b3d24")
turtle.pensize(6)
turtle.circle(35)
turtle.penup()
turtle.goto(-55,20)
turtle.pendown()
turtle.pensize(1)
turtle.dot(3)
for i in range(24):
    turtle.forward(27)
    turtle.backward(27)
    turtle.right(15)
turtle.right(90)
turtle.penup()
turtle.pensize(10)
turtle.pencolor("#342c1d")
turtle.goto(-62,-18)
turtle.pendown()
turtle.forward(37)
turtle.pencolor("#4b3d24")
turtle.penup()
turtle.goto(-55,20)
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(17)
turtle.left(90)
turtle.penup()
turtle.forward(150)
turtle.right(180)
turtle.pensize(5)
turtle.pencolor("gray")
turtle.forward(6)
turtle.pendown()
turtle.forward(145)
turtle.left(159)
turtle.forward(160)
turtle.mainloop()