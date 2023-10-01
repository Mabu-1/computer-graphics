import turtle
import math
t = turtle.Turtle()
radius = 100  
num_points = 360  
t.penup()
t.goto(radius, 0)  
t.pendown()
for _ in range(num_points):
    x = radius * math.cos(math.radians(_))
    y = radius * math.sin(math.radians(_))
    t.goto(x, y)


t.hideturtle()
turtle.exitonclick()
