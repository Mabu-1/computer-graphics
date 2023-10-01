import turtle
import math

t = turtle.Turtle()



radius = 100  
num_points = 360  

t.penup()
t.goto(radius, 0) 
t.pendown()

for _ in range(num_points):
    angle = math.radians(_)  
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    t.goto(x, y)


t.hideturtle()
turtle.exitonclick()
