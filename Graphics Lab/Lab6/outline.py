import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.title("Outline Font Rendering")
screen.setup(400, 200)

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Clear the canvas
t.penup()
t.goto(-200, -100)
t.pendown()
t.clear()

# Define font properties
font_size = 40
stroke_color = 'blue'

# Render outlined text
textToRender = "Mabu"
t.penup()
t.goto(-150, 0)
t.pendown()
t.color(stroke_color)
t.begin_fill()
t.write(textToRender, font=("Arial", font_size, "normal"))
t.end_fill()

# Close the turtle graphics window when clicked
turtle.exitonclick()
