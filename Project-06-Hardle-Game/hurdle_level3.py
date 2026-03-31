# Hurdle-03
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_round():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    if wall_in_front():
        one_round()
    else:
        move()