# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 6


def main():

    # words user input
    word1 = input("Enter word #1: ").lower().strip()
    word2 = input("Enter word #2: ").lower().strip()

    # converting strings to lists
    word1List = list(word1)
    word2List = list(word2)

    # checking if words are anagrams
    if len(word1) == len(word2) and word1List.sort() == word2List.sort():
        print("The words are anagrams!")
    else:
        print("The words are NOT anagrams.")


    # phrase user input
    phrase = input("\nEnter a phrase: ").lower().strip()

    # converting string to list
    phraseList = list(phrase)

    # removing spaces from list
    for element in phraseList:
        if element == " ":
          phraseList.remove(" ")

    # reversing list
    phraseListreversed = list()
    for i in range(len(phraseList) -1, -1, -1):
        letter = phraseList[i]
        phraseListreversed.append(letter)

    # comparing forwards with backwards
    if phraseList == phraseListreversed:
        print("The phrase is a palindrome!")
    else:
        print("The phrase is NOT a palindrome")


main()