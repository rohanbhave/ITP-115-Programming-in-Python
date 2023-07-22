# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# main_bhave_rohan.py
# Description:
# main file combining all functions

# importing files with other functions
import tasks
import interface

# name: main
# parameters: none
# return: none
# side effects: side effects of functions
# description: combines functions from tasks and interface files

def main():
    print("National Parks")

    # creating list of parks
    parksList = tasks.readParksFile()

    # getting dictionary for menu
    menuDict = interface.getMenuDict()

    # do while loop to display menu and user choice
    choice = "x"
    while choice.lower() != "q":
        print()
        # showing menu
        interface.displayMenu(menuDict)
        # letting user pick from menu
        choice = interface.getUserChoice(menuDict)

        # A -> All national parks
        if choice.lower() == "a":
            interface.printAllParks(parksList)

        # B -> Parks in a particular state
        if choice.lower() == "b":
            interface.printParksInState(parksList)

        # C -> The largest park
        if choice.lower() == "c":
            interface.printLargestPark(parksList)

        # D -> Search for a park
        if choice.lower() == "d":
            interface.printParksForSearch(parksList)


# calling main
main()





