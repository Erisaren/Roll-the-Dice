import time
import random
import raylib as rl

#  TODO
#  Find a solution to that circle
#  Have the result in the circle

def main():
    # Window title and dimensions
    WindowTitle = "*Roll the Die*".encode('utf-8')
    ScreenWidth = 800
    ScreenHeight = 600

    # Initialising the window and setting FPS
    rl.InitWindow(ScreenWidth, ScreenHeight, WindowTitle) # type: ignore
    rl.SetTargetFPS(60)

    roll = 0  # Dice roll result
    turn = 0  # Number of times rolled
    prompt_text = "Push 'r' for a random roll.\n\nPush 'n' to quit.".encode('utf-8')
    
    while not rl.WindowShouldClose():
        rl.BeginDrawing()
        rl.ClearBackground(rl.BLACK)

        # Draw greeting and instructions
        greeting = "Hello there!\n\nLet's roll a die to shake off boredom!".encode('utf-8')
        rl.DrawText(greeting, 100, 100, 24, rl.GREEN) # type: ignore
        rl.DrawCircle(400, 300, 100, rl.WHITE)
        # rl.DrawText(str(roll), 400, 300, 16, rl.GREEN) # type: ignore
        rl.DrawText(prompt_text, 100, 500, 24, rl.GREEN) # type: ignore

        # Check for user input
        if rl.IsKeyPressed(rl.KEY_R):
            roll = str(random.randint(1, 6))
            prompt_text = f"Your roll is {roll}!\n\n Push 'r' to roll again or 'n' to quit.".encode('utf-8')
            turn += 1

        elif rl.IsKeyPressed(rl.KEY_N):
            prompt_text = "Thank you for your participation!".encode('utf-8')
            rl.DrawText(prompt_text, 200, 575, 24, rl.RED) # type: ignore
            rl.EndDrawing()
            time.sleep(3)
            break

        # Check if turn limit is reached
        if turn == 9:
            prompt_text = "You have reached 9 turns already. Please take a break!".encode('utf-8')
            rl.DrawText(prompt_text, 100, 400, 16, rl.GREEN) # type: ignore
            rl.EndDrawing()
            time.sleep(3)
            break

        rl.EndDrawing()

    rl.CloseWindow()

if __name__ == "__main__":
    main()
