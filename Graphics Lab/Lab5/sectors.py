import turtle

# Create a turtle
t = turtle.Turtle()




radius = 100
angle = 90 


t.penup()
t.goto(0, -radius)
t.pendown()
t.begin_fill()
t.circle(radius, angle)
t.goto(0, 0)  
t.end_fill()


t.hideturtle()
turtle.done()
