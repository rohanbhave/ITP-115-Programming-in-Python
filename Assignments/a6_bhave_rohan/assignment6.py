# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Description
# This program prompts user to guess
# a word given jumbled letters


def main():

    # importing random function
    import random

    # creating lists
    words = ["jaguar", "water", "ukelele", "mirror"]
    hints = ["Luxury vehicle and animal", "dihydrogen monoxide", "guitar but smaller", "reflection"]

    # picking random word
    randomword = random.choice(words)
    words.index(randomword)

    # taking hint corresponding to random word
    randomhint = hints[words.index(randomword)]

    # turning word from string to list
    listrandom = list(randomword)

    # empty string for jumbled up word
    jumbled = ""


    # looping through each letter of word
    for element in range(0,len(randomword)):
        randomletter = random.choice(listrandom)
        jumbled = jumbled + randomletter    # adding random letter into jumbled word string
        listrandom.remove(randomletter)     # removing already used letter from original word
    print("The jumbled word is \"" + jumbled + "\"")

    # do while loop
    repeat = "yes"

    # counter to track number of guesses
    counter = 0

    # while loop for user input
    while repeat == "yes":
        guess = input("Enter your guess: ")
        counter = counter + 1
        if guess.lower() != randomword:     # if guess incorrect
            print("That is not correct")
            hint = input("Do you want a hint (y or n)? ")
            if hint.lower() == "y":
                print("The hint is \"" + randomhint + "\"")
        if guess.lower() == randomword:     # if guess correct
            print("You got it!")
            print("It took you", counter, "guesses.")
            repeat = "no"


main()