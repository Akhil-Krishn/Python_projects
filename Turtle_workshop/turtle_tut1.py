import turtle
import math

sqr_l = 100 #square length
sqr_d = math.sqrt((math.pow(sqr_l,2))*2) #square diameter
tri_l = sqr_l #triangle length same as square length for equilateral triangle

turtle.Screen()
turtle.pendown()
#drawing square
for i in range(4): 
    turtle.forward(sqr_l)
    turtle.left(90)
#first diagonal of square
turtle.left(45)
turtle.forward(sqr_d)
#triangle
turtle.left(75)
turtle.forward(tri_l)
turtle.left(120)
turtle.forward(tri_l)
#second diagonal of square
turtle.left(75)
turtle.forward(sqr_d)

turtle.penup()
turtle.mainloop()