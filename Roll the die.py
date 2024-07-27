import time
import random
import raylib as rl


def main():
    # Some variables here.
    roll = random.randint(1, 6)  # Dice rolls.
    turn = 0  # Number of time rolled.

    # Window title, dimensions.
    WindowTitle = "*Roll the Die*".encode('utf-8')
    ScreenWidth = 800
    ScreenHeight = 600

    # Initialising the window and setting FPS.
    rl.InitWindow(ScreenWidth, ScreenHeight, WindowTitle) # type: ignore
    rl.SetTargetFPS(60)

    while not rl.WindowShouldClose():
        # Basic greeting and screen position.
        greeting = "Hello there! We are going to roll a die in order to shake off boredom!\n".encode('utf-8')
        greeting_x = ScreenWidth/8
        greeting_y = ScreenHeight/6
        
        # Result screen will be a circle.
        circle_x = int(round(ScreenWidth/2))
        circle_y = int(round(ScreenWidth/2))
        circle_radius = 100

        # Button here.

        rl.BeginDrawing()
        rl.ClearBackground(rl.BLACK)
        # Draw green greeting text with font = 16.
        rl.DrawText(greeting, greeting_x, greeting_y, 16, rl.GREEN) # type: ignore
        # Drawing the result screen.
        rl.DrawCircle(circle_x, circle_y, circle_radius, rl.WHITE)
        #  Function in action.
        answer = str(input("Push \"r\" for a random roll."))
        while turn < 9:
            turn = turn + 1
            if answer == "r" or answer == "y":
                "Rolling the dices...\n")

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

        rl.EndDrawing()


def shutoff():
    rl.CloseWindow()