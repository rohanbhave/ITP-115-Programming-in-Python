# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Lab 9

# name: readFile
# desc: reads file with shows and genre
# parameters: genre, name of original file
# return: list with shows of certain genre
# side-effects: none

def readFile(userGenre, fileName):
    # opening file
    fileIn = open(fileName, "r")

    #creating lists for name and genre
    name = []
    genre = []

    # appending name and genre lists from original file
    for line in fileIn:
        line = line.strip()
        tempList = line.split(",")
        name.append(tempList[0])
        genre.append(tempList[1])

    index = 0
    userGenreList = []
    # creating list with shows of genre chosen by user
    for i in genre:
        if i == userGenre.lower():
            userGenreList.append(name[index])
        index = index + 1

    fileIn.close()
    return userGenreList

# name: writeFile
# desc: creating a file for user to view
# parameters: genre chosen by user, list of shows with chosen genre
# return: none
# side-effects: message to user about file

def writeFile(genre, showList):
    # opening file to write
    fileOut = open(genre + ".txt", "w")

    # printing to file
    for show in showList:
        print(show, file=fileOut)

    # message to user about file
    print("The file '" + genre + ".txt' has the following shows:")
    print(showList)


# name: main
# desc: combines read and write function
# parameters: none
# return: none
# side-effects: prompt to user

def main():

    # initial prompt to user
    print("TV Shows")
    genreOptions = "action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy"
    print("Possible genres are", genreOptions)

    # do while loop for user to pick a genre
    valid = False
    while not valid:
        userChoice = input("Enter a genre: ")
        if userChoice in genreOptions:
            valid = True

    # calling readFile and writeFile functions
    readFile(userChoice, "shows.csv")
    finalList = readFile(userChoice, "shows.csv")
    writeFile(userChoice, finalList)

main()


