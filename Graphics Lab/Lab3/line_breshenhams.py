import turtle



t = turtle.Turtle()


x1, y1 = -100, -50 
x2, y2 = 100, 50    


dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1


if dx > dy:
    p = dx / 2
    inc = dy
    end = dx
else:
    p = dy / 2
    inc = dx
    end = dy


t.penup()
t.goto(x1, y1)  
t.pendown()

for _ in range(int(end) + 1):
    t.goto(x1, y1)
    p -= inc
    if p < 0:
        x1 += sx
        y1 += sy
        p += end


t.hideturtle()
turtle.exitonclick()
