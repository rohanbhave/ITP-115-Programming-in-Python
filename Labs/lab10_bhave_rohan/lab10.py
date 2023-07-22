# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 10

# name: readFile
# parameters: name of text file
# return: dictionary
# side effects: none
# description:

def readFile(fileName):
    # creating empty dictionary
    letterDict = {}

    fileIn = open(fileName, "r")

    # looping through file
    for line in fileIn:
        line = line.strip()
        for word in line:
            for letter in word:
                letter = letter.lower()
                if letter.isalpha() is True:
                    if letter not in letterDict:
                        letterDict[letter] = 1
                    else:
                        letterDict[letter] = letterDict[letter] + 1

    fileIn.close()

    # returning empty dictionary
    return letterDict

# name: sortKeys
# parameters: dictionary of letters
# return: list of keys in alphabetical order
# side effects: none
# descriptiion: sorts list of keys in alphabetical order

def sortKeys(dictionary):
    # making list of keys
    dictKeys = list(dictionary.keys())

    # sorting value of keys
    dictKeys.sort()

    return dictKeys

# name: main
# parameters: none
# return: none
# side effects: none
# description: combines functions

def main():
    # calling functions
    letterCount = readFile("speech.txt")
    keyList = sortKeys(letterCount)

    print("The frequency of letters: ")
    # looping through sorted key
    for letter in keyList:
        # printing letter and count
        print(letter, ":", letterCount[letter])


main()
