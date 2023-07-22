# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# interface.py
# Description:
# Defining functions that will be called in other files

import tasks

# name: getMenuDict
# parameter: none
# return: dictionary where keys are letters for user input and values are description of menu options
# side effects: none
# description: creates a dictionary representing the menu

def getMenuDict():

    # creating dictionary
    menuDict = {}
    menuDict["A"] = "All national parks"
    menuDict["B"] = "Parks in a particular state"
    menuDict["C"] = "The largest park"
    menuDict["D"] = "Search for a park"
    menuDict["Q"] = "Quit"

    # returning dictionary representing menu
    return menuDict


# name: displayMenu
# parameter: dictionary for the menu
# return: none
# side effects: prints menu
# description: displays menu to user

def displayMenu(menuDict):
    # printing menu with for loop
    for key in menuDict:
        print(key, "->", menuDict[key])


# name: getUserChoice
# parameter: dictionary for menu
# return: string that is a valid choice entered by user
# side effects: prompt to user
# description: gets input from user that is in the menu choices

def getUserChoice(menuDict):
    # getting user input with error checking
    choice = " "
    while choice.upper() not in menuDict:
        choice = input("Choice: ").upper()

    # returning choice
    return choice


# name: printAllParks
# parameter: list of parks where each park is a dictionary
# return: none
# side effects: information about parks
# description: prints information about every park in dictionary

def printAllParks(parksList):
    # looping through park list
    for dictionary in parksList:
        print()
        print(dictionary["Name"], "(" + dictionary["Code"] + ")")   # name (code)
        print("\tLocation:", dictionary["State"])   # location
        print("\tArea:", dictionary["Acres"], "acres")  # area
        print("\tDate Established:", tasks.convertDate(dictionary["Date"])) # date


# name: getStateAbbr
# parameter: none
# return: a string with two-letter abbreviation of state
# side effects: prompt for user
# description: returns abbreviated version of state name

def getStateAbbr():
    # do while loop for user to enter input until input is two letters
    stateName = "x"
    while len(stateName) != 2:
        # user input
        stateName = input("Enter a state: ")

        # message for user to enter 2 letter abbreviation
        if len(stateName) != 2:
            print("Need the two letter abbreviation")

    # returning uppercase version of state name
    return stateName.upper()


# name: printParksInState
# parameter: list of parks where each park is a dictionary
# return: none
# side effects: prints park info
# description: prints parks from a specific state

def printParksInState(parksList):
    # calling getStateAbbr function
    state = getStateAbbr()

    # variable to track if any parks are in the state
    noPark = True

    # looping through list of parks
    for dictionary in parksList:
        # printing info about parks in state
        if dictionary["State"] == state:
            print()
            print(dictionary["Name"], "(" + dictionary["Code"] + ")")
            print("\tLocation:", dictionary["State"])
            print("\tArea:", dictionary["Acres"], "acres")
            print("\tDate Established:", tasks.convertDate(dictionary["Date"]))

            # indicator that there is at least one state as such
            noPark = False

    # message if no parks in state
    if noPark is True:
        print("There are no national parks in", state, "or it is not a valid state")


# name: printLargestPark
# parameters: list of parks where each park is a dictionary
# return: none
# side effects: park info
# description: prints information about the largest park

def printLargestPark(parksList):
    # calling getLargestPark function
    largestState = tasks.getLargestPark(tasks.readParksFile())

    # looping through list of parks to find dictionary with largest park
    for dictionary in parksList:
        # comparing park codes
        if dictionary["Code"] == largestState:
            # printing information
            print()
            print(dictionary["Name"], "(" + dictionary["Code"] + ")")
            print("\tLocation:", dictionary["State"])
            print("\tArea:", dictionary["Acres"], "acres")
            print("\tDate Established:", tasks.convertDate(dictionary["Date"]))
            print("\tDescription:", dictionary["Description"])


# name: printParksForSearch
# parameters: list of parks where each park is a dictionary
# return: none
# side effects: user prompt
# description: prints information about parks that contain search term in their information

def printParksForSearch(parksList):
    # getting search term from user
    term = input("Enter text for searching: ")

    # variable to keep track of if term is in any park info
    termPresent = False

    # looping through information about each park
    for dictionary in parksList:
        # comparing term with park information
        if term in dictionary["Code"] or term in dictionary["Name"] or term in dictionary["Description"]:
            print()
            print(dictionary["Name"], "(" + dictionary["Code"] + ")")
            print("\tLocation:", dictionary["State"])
            print("\tArea:", dictionary["Acres"], "acres")
            print("\tDate Established:", tasks.convertDate(dictionary["Date"]))
            print("\tDescription:", dictionary["Description"])

            # indicating that term is present in at least one park
            termPresent = True

    # if term not present in any park
    if termPresent is False:
        print("There are no national parks for the search text of '" + term + "'.")
