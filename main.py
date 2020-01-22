import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False 
range = 100

while not quit:
    print("\nHey there new player!")
    print("*waves*")
    print("\nWhat's your name? :)")
    myName = input()
    random_number = random.randint(1,range)
    count = 0  
    number = 1
    print("\nWell, "+ myName +", lets play a game!")  

    while number != random_number:
        number = input("\nTry guessing a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("\n*Sigh*...")
            print("\nCome on " + myName + ",that's NOT a number!")
            print("Let's try this again...")
        else:
            number= int(number)
            count = count + 1
            if number > random_number:
                print("\nHmmmm, that's not it.")
                print("(Hint) Your're too high!")
            elif number < random_number:
                print("\nSorry, that's not right.")
                print("(Hint) Your're too low!")
    print("\nWhooooooooooooooo!")
    print("Nice job " + myName +'!') 
    print("\nIt only took you {} tries...".format(count))
    play_again = input("\nWould you like to play again (yes or no)? ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y" :
        quit = False 
    else: 
        quit = True

print("\n*cries*...")
print("\n\nAlright, well thanks for playing "+ myName +"! See you later! & tell your friends about me!")

