# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Description
# This program simulates a game of
# rock, paper, scissors

# fn: displayRules
# desc: display rules of game to user
# input param: none
# return: none
# side-effects: game rules

def displayRules():
    print("Let's play Rock Paper Scissors")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("\tIf both the choices are the same, it's a tie")


# fn: getComputerNum
# desc: gets random number between 0 and 2
# input param: none
# return: random int between 0 and 2
# side-effects: none

import random

def getComputerNum():
    options = [0, 1, 2]
    return random.choice(options)


# fn: getPlayerNum
# desc: user inputs int
# input param: none
# return: int that represents user's choice
# side-effects: Options for user to pick

def getPlayerNum():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    user_choice = -1
    options = [0, 1, 2]
    while user_choice not in options:
        user_choice = int(input("> "))
    return user_choice


# fn: playRound
# desc: simulates game
# input param: int for computer's choice and int for user's choice
# return: int representing outcome of game
# side-effects: none


def playRound(computerNum, playerNum):
    # tie outcomes
    if computerNum == playerNum:
        return 0
    # player win outcomes
    elif computerNum == 0 and playerNum == 1:
        return 1
    elif computerNum == 1 and playerNum == 2:
        return 1
    elif computerNum == 2 and playerNum == 0:
        return 1
    # computer win outcomes
    elif playerNum == 0 and computerNum == 1:
        return -1
    elif playerNum == 1 and computerNum == 2:
        return -1
    elif playerNum == 2 and computerNum == 0:
        return -1


# fn: continueGame
# desc: allows user to continue if they want
# input param: none
# return: bool
# side-effects: none

def continueGame():
    keepPlaying = input("Do you want to continue player (y or n)? ")
    if keepPlaying.lower() == "y":
        return True
    else:
        return False


# fn: main
# desc: main function that runs the game
# input param: none
# return: none
# side-effects: results of game

def main():
    # counters
    ties = 0
    userWins = 0
    computerWins = 0

    # Keep playing
    keepPlaying = True

    # While loop to keep game running
    while keepPlaying is True:
        print("")
        displayRules()
        computer = getComputerNum()
        player = getPlayerNum()
        result = playRound(computer, player)
        if result == 1:
            print("You win!")
            userWins = userWins + 1
        elif result == -1:
            print("Computer wins.")
            computerWins = computerWins + 1
        elif result == 0:
            print("You and the computer tied.")
            ties = ties + 1
        keepPlaying = continueGame()

    # counter results
    print("\nYou won", userWins, "game(s).")
    print("The computer won", computerWins, "game(s).")
    print("You tied with the computer", ties, "time(s)")

# Calling main
main()