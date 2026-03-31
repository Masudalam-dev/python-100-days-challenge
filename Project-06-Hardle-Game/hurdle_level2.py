# Hurdle-02
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_round():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    one_round()