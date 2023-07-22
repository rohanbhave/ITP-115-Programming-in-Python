#Rohan Bhave, rbhave@usc.edu
#ITP 115, Spring 2022
#Section: 32096
#Lab 2

def main():

    #User input
    year = int(input("Enter year: "))

    #Calculating remainder
    number = year % 12

    #Branching statements mapping remainder to animal name
    if number == 0:
        animal = "Monkey"
    elif number == 1:
        animal = "Rooster"
    elif number == 2:
        animal = "Dog"
    elif number == 3:
        animal = "Pig"
    elif number == 4:
        animal = "Rat"
    elif number == 5:
        animal = "Ox"
    elif number == 6:
        animal = "Tiger"
    elif number == 7:
        animal = "Rabbit"
    elif number == 8:
        animal = "Dragon"
    elif number == 9:
        animal = "Snake"
    elif number == 10:
        animal = "Horse"
    elif number == 11:
        animal = "Goat"

    #Output to user
    print(year, "is the Year of the", animal + ".")
main()