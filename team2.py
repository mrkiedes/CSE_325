"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random


strategy_name = "Historical Choices"
                     
def move(my_history, their_history):
    # If its my first move then move randomly
    if len(my_history) == 0:
        pick = random.choice(["r", "p", "s"])
    elif len(my_history) == 1:
        # If I have moved once, then base my next move on their history
        match their_history[len(their_history) - 1]:
            case "r":
                pick = "p"
            case "p":
                pick = "s"
            case "s":
                pick = "r"
    else:
        # If we are on the second or further, look for a pattern with the last two moves
        # If a pattern is found, counterpick it.  Otherwise choose randomly.
        immediate_history = their_history[len(their_history) - 1] + their_history[len(their_history) - 2]
        if






    return pick