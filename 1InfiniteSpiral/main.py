import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Nekonečná spirála")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(300):
    t.color(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(59)

turtle.done()