import turtle


screen = turtle.Screen()

t = turtle.Turtle()




t.begin_fill()
t.color("yellow")  
t.circle(100)
t.end_fill()


t.penup()
t.goto(-40, 100)
t.pendown()
t.begin_fill()
t.color("red") 
t.circle(20)
t.end_fill()


t.penup()
t.goto(40, 100)
t.pendown()
t.begin_fill()
t.color("red") 
t.circle(20)
t.end_fill()




t.penup()
t.goto(40,60)
t.pendown()
t.right(120)
t.circle(-40, 116)


t.hideturtle()
turtle.exitonclick()
