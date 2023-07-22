# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 4

def main():

    # Establishing counter variables
    numSpace = 18
    numSymbols = 1

    # For loop
    for output in range (0, 10):
        print(" " * numSpace, "# " * numSymbols)
        # Changing counter every time
        numSpace = numSpace - 2
        numSymbols = numSymbols + 2

main()