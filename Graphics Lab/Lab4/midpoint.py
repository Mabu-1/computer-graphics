import turtle


t = turtle.Turtle()


radius = 100
x = 0
y = radius
p = 1 - radius




while x <= y:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(-x, y)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(x, -y)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(-x, -y)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(y, x)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(-y, x)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(y, -x)
    t.pendown()
    t.dot(5, "black")

    t.penup()
    t.goto(-y, -x)
    t.pendown()
    t.dot(5, "black")

    if p < 0:
        p += 2 * x + 3
    else:
        p += 2 * (x - y) + 5
        y -= 1
    x += 1

# Hide the turtle and keep the window open until manually closed
t.hideturtle()
turtle.done()
