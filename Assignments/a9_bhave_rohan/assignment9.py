# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Assignment 9
# Description
# This program translates from English to
# another language

# name: getAllLanguages
# parameters: string containing name of a csv file to read from
# return: list of strings representing language in header row
# side effects: none
# description: gets the header row of a csv file with languages

def getAllLanguages(fileName = "languages.csv"):
    # opening file
    fileIn = open(fileName, "r")
    # taking first line of file
    headerLine = fileIn.readline()
    # creating list out of first line of csv file
    languageList = headerLine.split(",")
    fileIn.close()
    return languageList


# name: getTranslationLanguage
# parameters: list of the languages
# return: string for language to translate words into
# side effects: languages available and prompt to user
# description: allows user to select a language

def getTranslationLanguage(languagesList):
    # showing user options
    print("Translate English words to one of the following languages:")
    languageDisplay = languagesList
    languageDisplay = languageDisplay[1:]
    languageOptions = (" ").join(languageDisplay)
    print(languageOptions)

    # while loop for user to pick a language
    userLanguage = " "
    while userLanguage.title() not in languageDisplay:
        userLanguage = input("Enter a language: ")
        if userLanguage.title() not in languageDisplay:
            print("This program does not support", userLanguage.title())

    return userLanguage.title()

# name: readDataFile
# parameters: list of languages, string with name of language, name of csv file
# return: list of words in language
# side effects: none
# description: generates list of

def readDataFile(languagesList, languageStr = "English", fileName = "languages.csv"):
    # creating empty list for words
    wordList = []

    # opening file
    fileIn = open(fileName, "r")

    # skipping first line
    headerLine = fileIn.readline()
    # languagesList = getAllLanguages("languages.csv")
    # languageStr = getTranslationLanguage()

    # determining index of language
    index = languagesList.index(languageStr)

    # looping through rest of file
    for line in fileIn:
        line = line.strip()
        lineList = line.split(",")
        wordList.append(lineList[index])

    fileIn.close()

    return wordList

# name: createTextFile
# parameters: name of language for translation
# return: none
# side effects: printing to output file
# description: creates output file

def createTextFile(language):
    # creating output file
    fileOut = open(language + ".txt", "w")
    print("Words translated from English to " + language, file=fileOut)

    # closing file
    fileOut.close()

# name: translateWords
# parameters: list of english words, list of words from other language, language of words for translation
# return: none
# side effects: feedback about word
# description: translates from English to other langauge

def translateWords(englishList, translationList, language):
    # opening output fie
    fileName = language + ".txt"
    fileIn = open(fileName, "a+")

    repeat = "y"
    while repeat.lower() == "y":
        # word for user wants to translate
        word = input("\nEnter a word to translate: ")

        # making sure word is in list
        if word not in englishList:
            print(word, "is not in the English list")
        else:
            # determining translation from english to other language
            index = englishList.index(word)
            translatedWord = translationList[index]

            # if there is a translation
            if translatedWord != "-":
                # printing to user
                print(word, "translates to", translatedWord)

                # printing to file
                print(word, "=", translatedWord, file=fileIn)
            # if there is no translation
            else:
                print(word, "does not have a translation")

        repeat = input("Another word (y or n)? ")

    # telling user name of output file
    print("\nTranslated words have been saved to", fileName)

# name: main
# parameters: none
# return: none
# side effects: none
# description: combines all functions

def main():
    # calling getAllLanguages function
    getAllLanguages()
    languageList = getAllLanguages()

    # calling readDataFile function
    readDataFile(languageList)
    englishWordList = readDataFile(languageList, "English")

    # calling getTranslationLanguage function
    userLanguage = getTranslationLanguage(languageList)

    # calling readDataFile function again
    readDataFile(languageList, userLanguage)
    languageWordList = readDataFile(languageList, userLanguage)

    # calling createTextFile function
    createTextFile(userLanguage)

    # calling translateWords function
    translateWords(englishWordList, languageWordList, userLanguage)

main()













