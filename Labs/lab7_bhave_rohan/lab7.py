# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 7

# defining rectangle function
def printRectangle(length, width):
    print(" " + "–" * width)
    for i in range(length):
        print(("|" + " " * width + "|"))
    print(" " + "–" * width)

# defining square function
def printSquare(size):
    print(" " + "–" * size)
    for i in range(size):
        print(("|" + " " * size + "|"))
    print(" " + "–" * size)

# defining main function with user input
def main():
    print("What shape would you like to print?")
    print("r) rectangle")
    print("s) square")
    shape = input("> ")

    # if user picks rectangle
    if shape.lower() == "r":
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        printRectangle(length, width)

    # if user picks square
    elif shape.lower() == "s":
        size = int(input("Enter the size: "))
        printSquare(size)

    # if user enters something else
    else:
        print("That shape is not supported.")

# calling main function
main()