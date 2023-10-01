import turtle
import math


t = turtle.Turtle()



a = 100  
b = 50   


t.penup()

for angle in range(0, 360, 5):
    x = a * math.cos(math.radians(angle))
    y = b * math.sin(math.radians(angle))
    t.goto(x, y)
    t.pendown()
    t.dot(5)
    t.penup()


t.hideturtle()
turtle.done()
