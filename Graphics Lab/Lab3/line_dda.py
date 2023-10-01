import turtle


t = turtle.Turtle()





x1, y1 = -100, -50  
x2, y2 = 100, 50  


dx = x2 - x1
dy = y2 - y1


steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)


x_increment = dx / steps
y_increment = dy / steps


t.penup()
t.goto(x1, y1)  
t.pendown()

for _ in range(steps + 1):
    t.goto(x1, y1)
    x1 += x_increment
    y1 += y_increment


t.hideturtle()
turtle.exitonclick()
