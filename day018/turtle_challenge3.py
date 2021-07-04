from turtle import Turtle, Screen
import random


def change_color():
    num = random.randint(0, len(colours) - 1)
    return colours[num]


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
tut = Turtle()
tut.shape("turtle")
tut.color("firebrick")
# Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
sides_to_draw = 3
sum_of_external_angles = 360

for _ in range(8):
    for turns in range(sides_to_draw):
        tut.forward(100)
        tut.right(sum_of_external_angles / sides_to_draw)
    sides_to_draw += 1
    tut.pencolor(change_color())

screen = Screen()
screen.exitonclick()
