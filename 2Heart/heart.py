import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart from Python")

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)
pen.hideturtle()

colors = ["#ff0055", "#ff3366", "#ff6699", "#ff99bb", "#ffccdd"]

def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

# Draw glowing heart layers
for size in range(18, 8, -2):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color(colors[size % len(colors)])
    
    first_point = True
    
    for i in range(0, 360):
        t = math.radians(i)
        x = heart_x(t) * size
        y = heart_y(t) * size
        
        if first_point:
            pen.penup()
            pen.goto(x, y - 40)
            pen.pendown()
            first_point = False
        else:
            pen.goto(x, y - 40)

# Small animated dots around the heart
dot = turtle.Turtle()
dot.speed(0)
dot.hideturtle()

for i in range(80):
    angle = i * 25
    radius = 120 + (i % 20)
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius
    
    dot.penup()
    dot.goto(x, y)
    dot.dot(4, colors[i % len(colors)])

# Text
pen.penup()
pen.goto(0, -230)
pen.color("white")
pen.write(
    "Made with Python Turtle",
    align="center",
    font=("Arial", 18, "bold")
)

turtle.done()