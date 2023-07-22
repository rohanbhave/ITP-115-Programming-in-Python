# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 5

def main():

    import random

    # Creating list for each type of word
    nouns = ["Person", "Place", "Thing", "potato"]
    verbs = ["danced", "ate", "frolicked"]
    adverbs = ["happily", "bravely", "cheerfully"]

    # Variable for do-while loop
    choice = 0

    # While loop
    while choice != 5:

        # Displaying menu
        print("Welcome to the Sentence Generator")
        print("1. View Words")
        print("2. Add Noun")
        print("3. Remove Verb")
        print("4. Generate sentence")
        print("5. Exit")

        # User input
        choice = int(input("> "))

        # Action based on what user chooses from menu
        if choice == 1:     # View words
            print("nouns:", nouns)
            print("verbs:", verbs)
            print("adverbs:", adverbs)
            print()
        elif choice == 2:   # Add noun
            word = input("Enter the word: ")
            if word not in nouns:
                nouns.append(word)
            print()
        elif choice == 3:   # Remove verb
            word = input("Enter the word: ")
            if word in verbs:
                verbs.remove(word)
            print()
        elif choice == 4:   # Genereate sentence
            print(random.choice(nouns), random.choice(verbs), random.choice(adverbs) + ".")
            print()
        elif choice == 5:   # Exit
            print("Thank you for using the Sentence Generator!")
        else:               # Invalid input
            print("Invalid choice")
            print()


main()
