import turtle

# Create a Turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (1 is slow, 0 is fastest)

# Draw a square
side_length = 100
angle = 90
sides = 4
for _ in range(sides):
    pen.forward(side_length)
    pen.right(angle)

# Move to a new position to draw the triangle
pen.penup()  # Lift the pen
pen.goto(150, 0)  # Move to a new position
pen.pendown()  # Lower the pen

# Draw a triangle
side_length = 100
angle = 120
sides = 3
for _ in range(sides):
    pen.forward(side_length)
    pen.left(angle)

# Close the Turtle graphics window when clicked
window.exitonclick()
