# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 8


import random

# name: coin
# desc: simualtes flip of coin
# parameters: none
# return: heads or tails
# side-effects: none

def coin():
    options = ["heads", "tails"]
    flip = random.choice(options)
    return flip

# name: experiment
# desc: simulates process of flipping coins
# parameters: none
# return: integer
# side-effects

def experiment():
    # counters
    flipCounter = 0
    headsCounter = 0

    # while loop
    while headsCounter < 3:
        flipCounter = flipCounter + 1
        side = coin()
        if side == "heads":
            headsCounter = headsCounter + 1
        else:
            headsCounter = 0

    return flipCounter

# name: main
# desc: runs experiment 10 times
# paramenters: none
# return: none
# side-effect: average number of flips to get 3 heads

def main():
    totalFlips = 0
    # simulating 10 times
    for i in range (0,11):
        flips = experiment()
        totalFlips = totalFlips + flips
    # return average
    return totalFlips/10

# program output to user
print("The average for 3 heads in a row is:", main())

