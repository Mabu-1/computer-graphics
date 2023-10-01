import turtle
t = turtle.Turtle()

t.begin_fill()
t.color("green")
for _ in range(2):  
    t.forward(160) 
    t.left(90)  
    t.forward(90)  
    t.left(90)  
t.end_fill()
t.penup()
t.goto(80,30)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(20)
t.end_fill()
t.hideturtle()  
# Close the turtle graphics window when clicked
turtle.exitonclick()
