import turtle



t = turtle.Turtle()


t.penup()
t.goto(-30,0)
t.pendown()
t.forward(60)
t.penup()
t.goto(0,0)
t.pendown()

t.right(135)  
t.forward(50)  
t.left(135)  
t.forward(50)  
t.left(120)  
t.forward(40) 

t.right(135)
t.forward(10)
t.circle(-18,100)
t.hideturtle()  


turtle.exitonclick()
