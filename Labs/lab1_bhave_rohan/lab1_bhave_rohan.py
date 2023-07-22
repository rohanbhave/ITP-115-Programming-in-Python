def main():
    #Rohan Bhave, rbhave@usc.edu
    #ITP 115, Spring 2022
    #Section: 3206
    #Lab 1

    #print statement using escape characters
    print("\"Do your little bit of good where you are; it's those little bits of \ngood put together that overwhelm the world.\"\n - Desmond Tutu \n")

    #User input day, month, and date
    day = input("Enter the day of the week: ")
    month = input("Enter the month: ")
    date = int(input("Enter the date: "))
    print("\n")

    #Message to user
    print("Today is " + day + ",", month, str(date) + ".")
    print("Tomorrow will be", month, str(date + 1) + ".")

main()