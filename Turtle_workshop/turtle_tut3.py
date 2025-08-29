import turtle
import random
turtle.Screen()
bigcircle_rad = 200
smallcircle_rad = 125
colour_lst = ['red',"green","orange","violet","pink","cyan","purple","indigo","blue"]
turtle.penup()
turtle.fillcolor("yellow")
turtle.goto(0,-bigcircle_rad)
turtle.begin_fill()
turtle.pendown()
turtle.circle(bigcircle_rad)
turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
for i in range(12):
    turtle.fillcolor(colour_lst[random.randint(0,8)])
    turtle.begin_fill()
    turtle.forward(bigcircle_rad)
    turtle.left(97.5)
    turtle.forward(52.210)
    turtle.left(97.5)
    turtle.forward(bigcircle_rad)
    turtle.end_fill()
    turtle.right(165)
turtle.penup()
turtle.fillcolor("#45ff02")
turtle.goto(0,-smallcircle_rad)
turtle.begin_fill()
turtle.pendown()
turtle.circle(smallcircle_rad)
turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
for i in range(4):
    turtle.fillcolor(colour_lst[random.randint(0,8)])
    turtle.begin_fill()
    turtle.forward(smallcircle_rad)
    turtle.left(135)
    turtle.forward(176.77)
    turtle.left(135)
    turtle.forward(smallcircle_rad)
    turtle.end_fill()
    turtle.right(180)
for i in range(4):
    val = 33
    if i == 0:
        codinate_x = val
        codinate_y = val
    elif i == 1:
        codinate_x = -val
        codinate_y = val
    elif i == 2:
        codinate_x = -val
        codinate_y = -val
    else:
        codinate_x = val
        codinate_y = -val
    turtle.pencolor(colour_lst[random.randint(0,8)])
    turtle.penup()
    turtle.goto(codinate_x,codinate_y)
    turtle.dot(30)
    turtle.pendown()
turtle.mainloop()