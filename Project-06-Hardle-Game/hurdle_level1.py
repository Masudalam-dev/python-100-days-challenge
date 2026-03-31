# Hurdle-01
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


for robot in range(6):
    one_round()