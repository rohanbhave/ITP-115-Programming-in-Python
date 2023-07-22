# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Description
# This program shows the chracter distribution
# of a setence that the user inputs

def main():
    # list with letters of the alphabet
    #alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet = "abcdefghijklmnopqrstuvqxyz"
    # Initial prompt for user
    print("Character Distribution")
    rounds = int(input("Enter the number of times to run: "))

    # Range-based loop allowing repetition
    for times in range(rounds):
        sentence = input("\nEnter a sentence: ")
        numspecial = 0  # Establishing counter for special characters

        # For loop counting special characters
        for character in sentence:
            if character.lower() not in alphabet and character != " ":
                numspecial = numspecial + 1

        # Printing number of special characters
        if numspecial > 0:
            print("Special characters:", "*" * numspecial)
        else:
            print("Special characters: NONE")

        # Outer for loop looping through each letter of the alphabet
        for letter in alphabet:
            numletter = 0   # Establishing counter for a letter

            # Inner for loop looping through each character of user input
            for character in sentence:
                if character.lower() == letter:
                    numletter = numletter + 1

            # Printing number of each letter of the aphabet in user input
            if numletter > 0:
                print(letter + ":", ("*" * numletter))
            else:
                print(letter + ":", "NONE")

main()