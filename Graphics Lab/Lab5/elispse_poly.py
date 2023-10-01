import turtle
import math
a = 100  
b = 50   
turtle.speed(0)


for _ in range(0, 360, 5):
    x = a * math.cos(math.radians(_))
    y = b * math.sin(math.radians(_))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5)


turtle.hideturtle()
turtle.done()
