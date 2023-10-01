import turtle


t = turtle.Turtle()




radius = 100
angle = 90 


t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius, angle)


t.hideturtle()
turtle.done()
