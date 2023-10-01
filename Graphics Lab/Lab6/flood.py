import turtle

# Function that returns true if the given pixel is valid
def isValid(screen, m, n, x, y, prevC, newC):
    if x < 0 or x >= m or y < 0 or y >= n or screen[x][y] != prevC or screen[x][y] == newC:
        return False
    return True

# FloodFill function
def floodFill(screen, m, n, x, y, prevC, newC):
    queue = []

    # Append the position of the starting pixel of the component
    queue.append([x, y])

    # Color the pixel with the new color
    screen[x][y] = newC

    # While the queue is not empty i.e. the whole component having prevC color is not colored with newC color
    while queue:

        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the adjacent pixels are valid
        if isValid(screen, m, n, posX + 1, posY, prevC, newC):
            # Color with newC if valid and enqueue
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])

        if isValid(screen, m, n, posX - 1, posY, prevC, newC):
            screen[posX - 1][posY] = newC
            queue.append([posX - 1, posY])

        if isValid(screen, m, n, posX, posY + 1, prevC, newC):
            screen[posX][posY + 1] = newC
            queue.append([posX, posY + 1])

        if isValid(screen, m, n, posX, posY - 1, prevC, newC):
            screen[posX][posY - 1] = newC
            queue.append([posX, posY - 1])

# Initialize Turtle Graphics
screen = turtle.Screen()
screen.title("Turtle Flood Fill Example")

# Create a Turtle object for drawing
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed

# Example grid
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

# Row of the display
m = len(grid)

# Column of the display
n = len(grid[0])

# Co-ordinate provided by the user
x = 4
y = 4

# Current color at that co-ordinate
prevC = grid[x][y]

# New color that has to be filled
newC = 3

# Draw the grid using Turtle Graphics
cell_size = 30
t.penup()
t.goto(-n * cell_size / 2, m * cell_size / 2)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(cell_size)
                t.right(90)
            t.end_fill()
        t.penup()
        t.forward(cell_size)
    t.goto(-n * cell_size / 2, t.ycor() - cell_size)

# Call floodFill to fill the grid with the replacement color
floodFill(grid, m, n, x, y, prevC, newC)

# Function to draw the updated grid
def draw_updated_grid():
    t.penup()
    t.goto(-n * cell_size / 2, m * cell_size / 2)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                t.pendown()
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            elif grid[i][j] == 2:
                t.pendown()
                t.begin_fill()
                t.fillcolor("blue")
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            elif grid[i][j] == 3:
                t.pendown()
                t.begin_fill()
                t.fillcolor("red")
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
            t.penup()
            t.forward(cell_size)
        t.goto(-n * cell_size / 2, t.ycor() - cell_size)

# Draw the updated grid
draw_updated_grid()

# Close the Turtle Graphics window when clicked
turtle.exitonclick()
