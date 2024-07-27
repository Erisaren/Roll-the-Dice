import time
import random
import raylib as rl



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
        # Result is in the circle
        roll_text = str(roll)
        roll_text_encoded = roll_text.encode('utf-8')
        text_width = rl.MeasureText(roll_text_encoded, 32) # type: ignore
        circle_x = 400
        circle_y = 300
        text_x = circle_x - text_width // 2
        text_y = circle_y - 20  # Half the font size (assuming 40)
        rl.DrawCircle(circle_x, circle_y, 100, rl.WHITE)
        rl.DrawText(roll_text_encoded, text_x, text_y, 32, rl.BLACK) # type: ignore
        rl.DrawText(prompt_text, 100, 500, 24, rl.GREEN) # type: ignore

        # Check for user input
        if rl.IsKeyPressed(rl.KEY_R):
            roll = str(random.randint(1, 6))
            prompt_text = "Push 'r' to roll again or 'n' to quit.".encode('utf-8')
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
            rl.DrawText(prompt_text, 75, 575, 24, rl.RED) # type: ignore
            rl.EndDrawing()
            time.sleep(5)
            break

        rl.EndDrawing()

    rl.CloseWindow()

if __name__ == "__main__":
    main()
