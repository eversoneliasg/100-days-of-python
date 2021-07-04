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


direction_heading_degrees = 5  # If you like, you can change the angle here and inside de loop
turt.speed("fastest")

for _ in range(int(360 / direction_heading_degrees)):
    turt.circle(100)
    turt.setheading(direction_heading_degrees)
    direction_heading_degrees += 5
    turt.color(random_color())

screen = Screen()
screen.exitonclick()
