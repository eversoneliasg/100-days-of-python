# Reeborg's World Maze
# Go to https://reeborg.ca/reeborg.html
# Choose Maze, at the top menu.
# Copy and paste the code below.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def follow_along_right_edge():
    if front_is_clear() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


while not at_goal():
    follow_along_right_edge()
