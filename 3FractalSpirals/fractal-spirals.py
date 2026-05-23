import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Fractal Spiral")


screen.setup(width=700, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

screen.tracer(0)

for i in range(2500):
    color = colorsys.hsv_to_rgb(i / 250, 1, 1)
    pen.color(color)

    pen.forward(i * 0.12)
    pen.right(89)


    if i % 25 == 0:
        pen.width(3)
    else:
        pen.width(1)

    if i % 5 == 0:
        screen.update()

screen.update()

turtle.done()