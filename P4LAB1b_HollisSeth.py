import turtle

#Create Turtle screen
window = turtle.Screen()
window.bgcolor("white")

#Create Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (1 is slow, 0 is fastest)
pen.pencolor("blue")  # Choose a color
pen.pensize(5)  # Choose a pen size

#Draw S
pen.forward(40)
pen.circle(50, 180)
pen.circle(-50, 180)
pen.forward(40)

#Draw H
pen.up()
pen.goto(100,0)
pen.down()
pen.setheading(90)
pen.forward(180)
pen.backward(75)
pen.right(90)
pen.forward(75)
pen.left(90)
pen.forward(75)
pen.backward(180)

#exit program
window.exitonclick()
