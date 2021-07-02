# The while loop looks like this:
# while something_is_true:
    # Do something repeatedly

# Go to https://reeborg.ca/reeborg.html
# Choose Hurdle 3, at the top menu, and paste the code below.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
