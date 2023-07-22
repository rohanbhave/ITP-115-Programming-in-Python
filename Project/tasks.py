# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section: 32096
# Final Project
# tasks.py
# Description:
# Defining task functions called from other functions in interface file

# name: readParksFile
# parameters: name of CSV file to read
# return: list of dictionaries each representing a park
# side effects: none
# description: transposes CSV file into dictionaries for each park

def readParksFile(fileName = "national_parks.csv"):
    # opening csv file
    fileIn = open(fileName, "r")

    # reading header line
    headerLine = fileIn.readline()
    headerLine = headerLine.strip()
    # converting header line into list
    headerList = headerLine.split(",")  # list of keys

    # creating empty list of parks
    parksList = []

    # lopping through rest of CSV file
    for line in fileIn:
        line = line.strip()
        # converting each line into a list
        lineList = line.split(",")

        # creating and modifying dictionary for each line
        dictionary = {}
        dictionary[headerList[0]] = lineList[0]     # code
        dictionary[headerList[1]] = lineList[1]     # name
        dictionary[headerList[2]] = lineList[2]     # state
        dictionary[headerList[3]] = lineList[3]     # acres
        dictionary[headerList[4]] = lineList[4]     # latitude
        dictionary[headerList[5]] = lineList[5]     # longitude
        dictionary[headerList[6]] = lineList[6]     # date

        # formatting description
        description = ",".join(lineList[7:])
        dictionary[headerList[7]] = description     # description

        # appending dictionary to list of parks
        parksList.append(dictionary)

    # closing file
    fileIn.close()

    # returning list of park dictionaries
    return parksList


# name: convertDate
# parameter: string containing the date
# return: string with formatted date
# side effects: none
# description: changes format of date

def convertDate(dataStr):
    # separating year, month, and day from dataStr
    yearNum = dataStr[0:4]
    monthNum = int(dataStr[5:7])
    dayNum = dataStr[8:10]

    # list with names of all months
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # converting month from number form to word form
    month = monthList[monthNum - 1]

    # putting together all parts of date
    date = month + " " + dayNum + ", " + yearNum

    # returning formatted data
    return date


# name: getLargestPark
# parameter: list of the parks where each park is a dictionary
# return: park code of the largest park
# side effects: none
# description: determines the largest park by area

def getLargestPark(parksList):
    maxAcre = 0
    # looping through list of parks
    for dictionary in parksList:
        acres = int(dictionary["Acres"])

        # finding park with maximum acres
        if acres > maxAcre:
            maxAcre = acres
            maxCode = dictionary["Code"]

    # returning code of the largest park
    return maxCode





