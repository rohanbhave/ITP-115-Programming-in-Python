#Rohan Bhave, rbhave@usc.edu
#ITP 115, Spring 2022
#Section 32096
#Description
#This program creates a Mad Libs Story
#It uses inputs from the user to complete the story.

def main():

    #Directions for user
    print("Type words in all lowercase and press enter ")
    #Words inputted by user
    word1 = input("Enter an adjective: ")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number greater than 0: "))
    word2 = input("Enter an item of clothing: ")
    word3 = input("Enter a singular noun: ")
    word4 = input("Enter an adverb ending in -ly: ")
    word5 = input("Enter plural objects: ")
    num3 = int(input("Enter a number greater than 0: "))
    num4 = float(input("Enter a price without dollar sign: "))

    #Story output to user
    print("\nRigel Goes on an Adventure \n")
    print("Once upon a time, Rigel, a", "\"" + word1 + "\"", "student at USC, was bored on a Saturday morning and decided he needed something to do.")
    print("All", "\"" + str(num2) + "\"", "of his friends were not available to hang out with him for some strange reason.")
    print("He finally decided to go to downtown Los Angeles for the day.")
    print("Rigel had only been there", "\"" + str(num1) + "\"", "times before so he was looking forward to it.")
    print("He put on his", "\"" + word2 + "\",", "got into his car and set the GPS for downtown LA.")
    print("As he arrived, Rigel was surprised when he saw a", "\"" + word3 + "\"" + ".")
    print("He'd never seen one before and wasn't sure what to do so he", "\"" + word4 + "\"", "stared.")
    print("First, Rigel decided to go into a store.")
    print("He'd always wanted to buy", "\"" + word5 + "\"", "so he spent", "$" + str(num3*num4), "on", "\"" + str(num3) + "\"", "\"" + word5 + "\"", "for", "\"" + "$" + str(num4) + "\"", "each.")
    print("Rigel was overly satisfied with himself and lived happily ever after.")

main()
