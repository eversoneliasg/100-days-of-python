from turtle import Turtle, Screen

the_turtle = Turtle()

the_turtle.shape("turtle")
the_turtle.color("firebrick")
# Drawing a dashed line interspersed with blank spaces

for _ in range(25):
    the_turtle.pendown()
    the_turtle.forward(5)
    the_turtle.penup()
    the_turtle.forward(5)

screen = Screen()
screen.exitonclick()
