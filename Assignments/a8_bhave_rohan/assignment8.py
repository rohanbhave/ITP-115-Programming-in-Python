# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Description
# This program simulates a game of
# tic tac toe

import TicTacToeHelper

# name: isValidNumber
# description: checks position variable
# parameters: list representing board, int corresponding to index position picked by user
# return: bool
# side-effects: none


def isValidNumber(boardList, position):
    # checking if position is from 0 to 8
    if position in range(0, 9):
        # checking if position is already taken by x or o
        if boardList[position] in ["x", "o"]:
            return False
        else:
            return True
    # returning false otherwise (to make while loop run later on)
    else:
        return False


# name: updateBoard
# description: places player's letter on board
# parameters: boardList, position, string representing user's letter
# return: none
# side-effects: none

def updateBoard(boardList, position, playerLetter):
    # replacing position with playerLetter on board
    del boardList[position]
    boardList.insert(position, playerLetter)


# name: playGame
# description: simulates Tic Tac Toe
# parameters: none
# return: none
# side-effects: game boards and result

def playGame():
    # list with numbers for board
    boardNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # move counter
    totalMoves = 0
    # if there is a winner or not yet
    winner = "n"

    # printing board
    TicTacToeHelper.printUglyBoard(boardNumbers)

    # while there is no winner
    while winner == "n":

        # alternating variable between whose move it is
        if totalMoves % 2 == 0:
            turn = "x"
        else:
            turn = "o"

        # while loop for one turn
        valid = False
        while not valid:
            # player x's turn
            if turn == "x":
                move = int(input("Player x, enter a number: "))
            # player o's turn
            elif turn == "o":
                move = int(input("Player o, enter a number: "))

            # checking if valid
            valid = isValidNumber(boardNumbers, move)

            # updating board and total moves if valid
            if valid is True:
                updateBoard(boardNumbers, move, turn)
                totalMoves = totalMoves + 1

        # printing updated board
        TicTacToeHelper.printUglyBoard(boardNumbers)


        # checking for winner
        TicTacToeHelper.checkForWinner(boardNumbers, totalMoves)

        # controlling while loop
        winner = TicTacToeHelper.checkForWinner(boardNumbers, totalMoves)

    # message to players after game is over
    print("Game Over!")

    if winner == "s":
        print("Stalemate reached")
    elif winner == "x":
        print("Player x is the winner")
    elif winner == "o":
        print("Player o is the winner")


# name: main
# description: allows user to keep playing rounds
# parameters: none
# return: none
# side-effects: prompt to play again

def main():
    print("Let's play Tic Tac Toe!")
    playAgain = "y"
    # do while loop to keep game running as long as players want
    while playAgain == "y":
        playGame()
        playAgain = input("Would you like to pay another round (y or n)? ").lower()

    print("Goodbye!")

main()
