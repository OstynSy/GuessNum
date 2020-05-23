import random
import sys

tries = 0
# start while loop
while True:
    variable = 0
    try:
        variable = int(input("Choose a number between 1 and 10 \n"))
        if variable < 1 or variable > 10:
            print("Invalid input")
            continue
    except ValueError:
        print("Invalid input")

# selects a random number between 1-10
    rand_num = random.randint(1, 10)
    tries += 1

    if variable == rand_num:
        print("Congratulations! You guessed the right number!")
        print("It took you " + str(tries) + " guesses!")
        tries = 0
    else:
        print("Better luck next time, \nthe number was: " + str(rand_num))

# play again while loop
    while True:
        choice = input("\nDo you want to play again? (yes/no) \n")
        if choice == "yes":
            break
        elif choice == "no":
            print("Thanks for playing")
            sys.exit()
        else:
            print("Invalid input")

