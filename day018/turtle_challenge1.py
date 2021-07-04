from turtle import Turtle, Screen

the_turtle = Turtle()

the_turtle.shape("turtle")
the_turtle.color("firebrick")
# Drawing a square
for _ in range(4):
    the_turtle.forward(200)
    the_turtle.right(90)

screen = Screen()
screen.exitonclick()
