import turtle



t = turtle.Turtle()

slope = 2  
c = 10  

for x in range(20, 25):  
    y = slope * x + c
    t.goto(x, y)


t.hideturtle()
turtle.exitonclick()
