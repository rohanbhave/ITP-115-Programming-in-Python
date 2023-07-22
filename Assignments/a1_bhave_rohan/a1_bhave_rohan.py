def main():

    #Rohan Bhave, rbhave@usc.edu
    #ITP 115, Spring 2022
    #Section: 32096
    #Assignment 1
    #Description: Printing Two Truths and a Lie

    #name
    first = "Rohan"
    last = "Bhave"

    #two truths and a lie statements
    statement1 = "I met Joe Biden as a kid"
    statement2 = "I have titanium plating in my arm"
    statement3 = "I once contracted the swine flu pandemic"

    #truth or lie corresponding to each of 3 statements
    truth1 = False
    truth2 = True
    truth3 = True

    #number of pets and siblings
    pets = 0
    siblings = 1

    #print statements
    #full Name
    print("Full name:",first, last, end="\n\n")

    #number of pets and siblings
    print("Number of pets:",pets)
    print("Number of siblings:",siblings, end="\n\n")

    #two truths and a lie statements
    print("Statement 1:",statement1,end="\n")
    print("Statement 2:",statement2,end="\n")
    print("Statement 3:",statement3,end="\n\n")

    # truth or lie corresponding to each of 3 statements
    print("Statement 1 is", truth1, end="\n")
    print("Statement 2 is", truth2, end="\n")
    print("Statement 3 is", truth3, end="\n")

main()

