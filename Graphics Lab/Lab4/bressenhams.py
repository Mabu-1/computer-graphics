import turtle

turtle.speed(0)  
radius = 100

x, y = 0, radius
d = 3 - 2 * radius

while x <= y:
  
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, "black")

   
    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    turtle.dot(5, "black")

    
    turtle.penup()
    turtle.goto(x, -y)
    turtle.pendown()
    turtle.dot(5, "black")

    
    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    turtle.dot(5, "black")

   
    turtle.penup()
    turtle.goto(y, x)
    turtle.pendown()
    turtle.dot(5, "black")

   
    turtle.penup()
    turtle.goto(-y, x)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(y, -x)
    turtle.pendown()
    turtle.dot(5, "black")

    # Octant 6
    turtle.penup()
    turtle.goto(-y, -x)
    turtle.pendown()
    turtle.dot(5, "black")

    if d <= 0:
        d = d + 4 * x + 6
    else:
        d = d + 4 * (x - y) + 10
        y -= 1
    x += 1


turtle.done()
