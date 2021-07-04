# import colorgram
#
# Commented because we don't need to run this everytime. We already ran once and got the list.
# colors_from_image = colorgram.extract('image.jpg', 20)
# rgb_tuple_list = []
#
# for color in colors_from_image:
#   temp_list_color = list(color.rgb)
#   color_tuple = tuple(temp_list_color)
#   rgb_tuple_list.append(color_tuple)
#
# print(rgb_tuple_list)

import turtle
import random

rgb_tuples = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112),
              (215, 130, 165), (215, 56, 27)]

turtle.colormode(255)


def random_color():
    random_rgb = random.choice(rgb_tuples)
    return random_rgb


def draw_dot(t):
    t.dot(20, random_color())
    t.forward(50)


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.penup()
my_turtle.speed("fastest")
my_turtle.hideturtle()  # This is optional

initial_height = -220
const_width = -220
gap = 50

for i in range(10):
    my_turtle.goto(const_width, initial_height)
    for j in range(10):
        draw_dot(my_turtle)
    initial_height += gap

screen = turtle.Screen()
screen.exitonclick()
