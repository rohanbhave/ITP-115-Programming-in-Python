# Rohan Bhave, rbhave@usc.edu
# ITP 115, Spring 2022
# Section 32096
# Description
# This program will determine the smallest and largest number
# entered by the user


def main():

    # Variable to make sure loop runs at least once
    keepgoing = "yes"

    while keepgoing == "yes":
        # Establishing value of variables as zero
        num_min = 0
        num_max = 0
        count = 0
        sum = 0
        num_user = 0

        # Prompt for user
        print("Input an integer greater than of equal to 0 (or -1 to quit): ")
        while num_user != -1:
            num_user = int(input("> "))

            # Making sure first input is both min and max
            if count == 0:
                num_max = num_user
                num_min = num_user
            if num_user >= 0:
                if num_user > num_max:  # Determining maximum
                    num_max = num_user
                if num_user < num_min:  # Determining minimum
                    num_min = num_user
                sum = sum + num_user  # Sum
                count = count + 1  # Counter

        # Output to user at end of a round
        print("The largest number is", num_max)
        print("The smallest number is", num_min)
        print("The average number is", (sum/count))
        repeat = input("\nWould you like to enter another set of numbers (y/n)? ")

        # Keeping outer while loop running if
        if repeat.lower() == "y":
            keepgoing = "yes"
        else:
            keepgoing = "no"

    # Out of outer loop
    print("\nGoodbye!")

main()