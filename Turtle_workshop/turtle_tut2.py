import turtle
#dimensions of the flag
rect_l = 200
rect_b = 50
#main setup
turtle.Screen()
turtle.pendown()
#drawing rectangles
for i in range(3): 
    turtle.goto(0,i*-50)
    hor = False #is True if a horizontal(length of rect) is drawn
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
#drawing ashoka chakra outline
turtle.penup()
turtle.goto(100,-45)
turtle.pendown()
turtle.dot(2)
turtle.pencolor("#27379b")
turtle.pensize(7)
turtle.circle(20)
#dot in the middle
turtle.penup()
turtle.goto(100,-25)
turtle.pendown()
turtle.dot(5)
#drawing the 24 lines
turtle.pensize(1)
for i in range(24):
    turtle.forward(20)
    turtle.backward(20)
    turtle.right(15)
#endloop
turtle.mainloop()