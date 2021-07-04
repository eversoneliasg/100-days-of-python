import turtle
from turtle import Turtle, Screen
import random

turt = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
turt.pensize(15)
turt.speed("fastest")

for _ in range(100):
    turt.color(random_color())
    turt.forward(40)
    turt.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
