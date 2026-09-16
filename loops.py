import turtle

# Set up the screen
window = turtle.Screen()

# Create your turtle object
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

# CRITICAL: This keeps the window open until you click inside it
window.exitonclick()
