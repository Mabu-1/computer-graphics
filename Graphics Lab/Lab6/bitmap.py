import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.title("Bitmap Font Rendering")
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Define the bitmap font texture as an array of characters
fontTexture = [
    "0011111000111110",
    "0011001100110011",
    "0110001100110001",
    "0110001100111111",
    "0110001100110011",
    "0011001100110011",
    "0011111000110011",
]

# Define character width and height
charWidth = 8
charHeight = 7

# Function to render a character at a specified position
def renderCharacter(character, x, y):
    for row in range(charHeight):
        for col in range(charWidth):
            pixel = fontTexture[row][col]
            if pixel == '1':
                t.penup()
                t.goto(x + col, y - row)  # Adjust coordinates for Turtle graphics
                t.pendown()
                t.dot()

# Function to render text using the bitmap font
def renderText(text, x, y):
    xOffset = 0
    for char in text:
        renderCharacter(char, x + xOffset, y)
        xOffset += charWidth + 1  # Add spacing

# Clear the canvas
t.penup()
t.goto(-200, 100)
t.pendown()
t.clear()

# Render text using the bitmap font
textToRender = "Mabu"
xStart = -150
yStart = 50
renderText(textToRender, xStart, yStart)

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window when clicked
screen.exitonclick()
