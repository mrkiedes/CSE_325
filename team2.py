"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random


strategy_name = "Historical Choices"

def basic_move(their_history):
    match their_history[len(their_history) - 1]:
        case "r":
            pick = "p"
        case "p":
            pick = "s"
        case "s":
            pick = "r"

def historical_move(their_history):
    temp = 1

def move(my_history, their_history):
    # Default case
    pick = random.choice(["r", "p", "s"])
    # If its my first move then move randomly
    print("Length of their history " + str(len(their_history)))

    if len(my_history) <= 1:
        # If I have moved once, then base my next move on their history
        print("1 Case")
        basic_move(their_history)
    else:
        # If we are on the second or further, look for a pattern with the last two moves
        # If a pattern is found, counterpick it.  Otherwise choose randomly.
        immediate_history = their_history[len(their_history) - 1] + their_history[len(their_history) - 2]
        if immediate_history[-2] == immediate_history[-1]:
            if immediate_history[-2] == "r":
                pick = "p"
            if immediate_history[-2] == "p":
                pick = "s"
            if immediate_history[-2] == "s":
                pick = "r"

        # If no pattern, pick based on their last entry
        else:
            basic_move(their_history)
    return pick