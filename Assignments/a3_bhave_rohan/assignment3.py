#Rohan Bhave, rbhave@usc.edu
#ITP 115, Spring 2022
#Section 32096
#Assignment 3
#Description:
#This program creates a Harry Potter vending machine.
#It determines the change and gives a discount.

def main():
    #Initial display to user
    print("Please select an item from the vending machine")
    print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
    print("\tb) Butterbeer for 2 sickles")
    print("\tc) Quill for 6 sickles")
    print("\td) Daily Prophet for 5 knuts")

    #User answer to prompt
    choice = input("Choice: ")

    #Storing item and cost
    a = ("Assortment of Candy")
    acost = int((7*1)+(11*29))
    b = ("Butterbeer")
    bcost = int(2*29)
    c = ("Quill")
    ccost = int(6*29)
    d = ("Daily Prophet")
    dcost = int(5*1)

    #Error checking user input
    if choice.lower() not in ["a", "b", "c", "d"]:
        item = c
        cost = ccost
        print("You entered an invalid choice, thus the item selected is the Quill\n")

    #Money user input
    print("\nPlease pay by entering the number of each coin ")
    galleons = int(input("Number of galleons: "))
    sickles = int(input("Number of sickles: "))
    knuts = int(input("Number of knuts: "))

    #Displaying cost in knuts
    if choice.lower() == "a":
        item = a
        cost = acost
        print("\nCost in knuts:",cost)
    elif choice.lower() == "b":
        item = b
        cost = bcost
        print("\nCost in knuts:",cost)
    elif choice.lower() == "c":
        item = c
        cost = ccost
        print("\nCost in knuts:",cost)
    elif choice.lower() == "d":
        item = d
        cost = dcost
        print("\nCost in knuts:",cost)

    #Displaying payment total
    payment = (galleons*493)+(sickles*29)+(knuts*1)
    print("Payment in knuts:",payment)

    #Comparing cost and payment
    if cost > payment:
        print("You did not enter enough money and will not receive the", item)
    #Change due if payment covers cost
    else:
        print("\nYou purchased the", item)

        change = payment-cost
        print("Your change is", change, "knuts")

        #Breaing down change into different coins
        print("You will be given")
        changegalleons = change//493
        change = change%493
        print("\tGalleons:",changegalleons)
        changesickles = change//29
        change = change%29
        print("\tSickles:", changesickles)
        changeknuts = change
        print("\tKnuts:", changeknuts)
main()