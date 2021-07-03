# Import example
# import pokedex
# print(pokedex.another_variable)

# Importing Turtle
# You can learn more about this library by consulting its documentation: https://docs.python.org/3/library/turtle.html
# import turtle OR

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)  # This will print the object showing his memory position
timmy.shape("turtle")  # Timmy's shape
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()  # Screen is where our turtle will be shown
print(my_screen.canvheight)  # Printing the attribute height of the screen
my_screen.exitonclick()  # Allows the programming to run until we click
