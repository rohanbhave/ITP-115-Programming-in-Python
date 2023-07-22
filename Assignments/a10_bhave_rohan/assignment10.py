# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Assignment 10
# Description
# This program manages a user's music library

import MusicLibraryHelper
import random

# name: displayMenu
# parameters: none
# return: none
# side effects: menu options for user
# description: displays menu

def displayMenu():
    print("\nManage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")

# name: displayLibrary
# parameters: dictionary representing music library
# return: none
# side effects: entire music library
# description: displays entire music library

def displayLibrary(dictionary):
    for key in dictionary:
        print("Artist:", key)
        print("\tAlbums:")
        for item in dictionary[key]:
            print("\t\t" + item)

# name: displayArtists
# parameters: dictionary representing music library
# return: none
# side effects: artists in music library
# description: displays artists in music library

def displayArtists(dictionary):
    print("Artists:")
    for key in dictionary:
        print("\t" + key)

# name: addAlbum
# parameters: dictionary representing music library
# return: none
# side effects: user input
# description: allows user to add album to dictionary

def addAlbum(dictionary):
    # user input for what artist and album they want to add
    artist = input("Enter artist: ")
    album = input("Enter album: ")

    # correcting to title case
    artist = artist.title()
    album = album.title()

    # adding album to list if album not there
    if artist in dictionary:
        dictionary[artist].append(album)
    # adding album to list if artist and album not there
    elif artist not in dictionary:
        dictionary[artist] = []
        dictionary[artist].append(album)


# name: deleteAlbum
# parameters: dictionary representing music library
# return: boolean if successful or not
# side effects: user input
# description: allows user to remove album from dictionary

def deleteAlbum(dictionary):
    # user input for what artist and album they want to delete
    artist = input("Enter artist: ")
    album = input("Enter album: ")

    # correcting to title case
    artist = artist.title()
    album = album.title()

    # removing album if in dictionary
    if artist in dictionary:
        if album in dictionary[artist]:
            dictionary[artist].remove(album)
            return True
    # returning false if function not successful
    else:
        return False

# name: deleteArtist(dictionary)
# parameters: dictionary representing music library
# return: boolean if successful or not
# side effects: user input
# description: removes artist from dictionary

def deleteArtist(dictionary):
    # user input for what artist they want to delete
    artist = input("Enter artist to delete: ")
    artist = artist.title()

    # removing artist if in dictionary
    if artist in dictionary:
        del dictionary[artist]
        return True
    # returning False is function not successful
    else:
        return False


# name: generateRandomPlaylist
# parameters: dictionary representing music library
# return: none
# side effects: displays random playlist to user
# description: generates a random playlist

def generateRandomPlaylist(dictionary):
    print("Here is your random playlist: ")

    # looping through dictionary and picking one random album from energy artist
    for artist in dictionary:
        randomAlbum = random.choice(dictionary[artist])
        print("\t" + randomAlbum, "by", artist)

# name: main
# parameters: none
# return: none
# side-effects:
# description: combines all functions

def main():
    # creating music dictionary
    musicDictionary = MusicLibraryHelper.loadLibrary("music_library.dat")

    keepDisplay = True

    # while loop to keep displaying menu
    while keepDisplay is True:
        displayMenu()

        # getting user choice
        choice = input("Choice: ")

        # calling functions based on user choice
        # display library
        if choice.lower() == "a":
            displayLibrary(musicDictionary)

        # display artists
        elif choice.lower() == "b":
            displayArtists(musicDictionary)

        # add artist/album
        elif choice.lower() == "c":
            addAlbum(musicDictionary)

        # delete album
        elif choice.lower() == "d":
            delAlbum = deleteAlbum(musicDictionary)

            # message to user
            if delAlbum is True:
                print("Delete album success")
            elif delAlbum is False:
                print("Delete album failed")


        # delete artist
        elif choice.lower() == "e":
            delArtist = deleteArtist(musicDictionary)

            # message to user
            if delArtist is True:
                print("Delete artist success")
            elif delArtist is False:
                print("Delete artist failed")


        # generate a random playlist
        elif choice.lower() == "f":
            generateRandomPlaylist(musicDictionary)

        # exit
        elif choice.lower() == "g":
            keepDisplay = False

        # invalid choice
        else:
            print("Invalid entry")

    # asking user to file name for music library
    libraryFile = input("Enter music library filename: ")

    # saving music library in file
    MusicLibraryHelper.saveLibrary(libraryFile, musicDictionary)
    print("Saved music library to", libraryFile)


main()
