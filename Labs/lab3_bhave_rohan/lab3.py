# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Lab 3

def main():

    # establishing value of variable outside loop
    userchoice = "x"

    # while loop, should only stop if user says to quit
    while userchoice.lower() != "q":
        # Showing user options
        print("What would you like to know?")
        print("a) Favorite Animal")
        print("f) Favorite food")
        print("p) Favorite Place")
        print("q) Quit")
        # user input
        userchoice = input("> ")

        # output to user
        if userchoice.lower() == "a":
            print("My favorite animal is a dog.\n")
        elif userchoice.lower() == "f":
            print("My favorite food is pasta.\n")
        elif userchoice.lower() == "p":
            print("My favorite place is my room.\n")
        elif userchoice.lower() == "q":
            print("Goodbye\n")
        else:
            print("That option is not available.\n")

main()
