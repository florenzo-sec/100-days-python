
# Reeborg's Lost Maze Solution
#The following code allows Reeborg to navigate through a maze using the right-hand rule.
#the functions turn_left(), move(), at_goal(), front_is_clear(), and right_is_clear() are predefined in Reeborg's environment.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()