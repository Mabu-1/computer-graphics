import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Set the turtle's properties
t.speed(1)  # Set the drawing speed (1 is slow, 10 is fast)
t.penup()
t.goto(-40, -150)  # Move to the starting position
t.pendown()

# Draw the base of Shahid Minar
t.color("black")
t.begin_fill()
t.forward(80)
t.right(90)
t.forward(10)
t.right(90)
t.forward(80)
t.right(90)
t.forward(10)
t.end_fill()

# Draw the central structure
t.penup()
t.goto(0, -80)
t.pendown()
t.begin_fill()
t.goto(-15, 60)
t.goto(15, 60)
t.goto(0, -80)
t.end_fill()

# Draw the floral designs
t.penup()
t.goto(0, 40)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(40)
t.end_fill()

# Hide the turtle and exit on click
t.hideturtle()
screen.exitonclick()
