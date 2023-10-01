import turtle

def boundary_fill(pos_x, pos_y, boundary_color, fill_color):
    current_color = turtle.Screen().getpixel(pos_x, pos_y)
    
    if current_color != boundary_color and current_color != fill_color:
        turtle.Screen().setpixel(pos_x, pos_y, fill_color)
        
        # Move to adjacent pixels and perform the same function
        boundary_fill(pos_x + 1, pos_y, boundary_color, fill_color)
        boundary_fill(pos_x - 1, pos_y, boundary_color, fill_color)
        boundary_fill(pos_x, pos_y + 1, boundary_color, fill_color)
        boundary_fill(pos_x, pos_y - 1, boundary_color, fill_color)

# Initialize the Turtle screen
screen = turtle.Screen()
screen.setup(400, 400)  # Set the screen size (adjust as needed)

# Set the boundary and fill colors (use RGB values or color names)
boundary_color = "black"
fill_color = "blue"

# Call the boundary fill function starting at the desired position
boundary_fill(0, 0, boundary_color, fill_color)

# Close the Turtle graphics window when done
screen.exitonclick()
