import time
import random
roll = random.randint(1, 6)  # Dice rolls.
turn = 0  # Number of time rolled.

#  Basic greetings.
print("Hello there! We are going to roll a die in order to shake off boredom!\n")

#  Function in action.
answer = str(input("Push \"r\" for a random roll."))
while turn < 9:
    turn = turn + 1
    if answer == "r" or answer == "y":
        print("Rolling the dices...\n")
        time.sleep(3)
        print("Your roll is ", roll, "!\n")
        answer = str(input("Roll the die again?\nPush \"y\" for yes.\nPush \"n\" for no."))
    elif answer == "n":
        print("Understood!")
        break
    else:
        redo = str(input("Roll the dice again?\nPush \"y\" for yes.\nPush \"n\" for yes."))
        break

if turn == 9:
    print("Die rolling can't be addictive but please, take a break.")

print("Thank you for your participation!")
