#  Variables.
import random
roll = random.randint(1, 6)  # Dice rolls.
turn = 0  # Number of time rolled.

#  Basic greetings.
print("Hello there! We are going to roll dice in order to shake off boredom!\n")

#  Function in action.
answer = str(input("Push \"r\" for a random roll."))
while turn < 9:
    turn = turn + 1
    if answer == "r" or answer == "y":
        print("Rolling the dices...\n")
        print("Your roll is ", roll, "!\n")
        answer = str(input("Roll the dice again?\nPush \"y\" for yes.\nPush \"n\" for no."))
    elif answer == "n":
        print("Understood!")
        break
    else:
        redo = str(input("Roll the dice again?\nPush \"y\" for yes.\nPush \"n\" for yes."))
        break

if turn == 9:
    print("Dice rolling can't be addictive but please, take a break.")

print("Thank you for your participation!")
