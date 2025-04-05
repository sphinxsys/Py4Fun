'''
A simple console-based Snake game using the curses library.
To control the snake using arrow keys. 

The goal is to eat food (represented by a character) and grow the snake while 
avoiding collisions with the walls and itself. 
The game ends when the snake collides with itself or the walls, and a message is
displayed before exiting.

https://docs.python.org/3/howto/curses.html
install curses library if not already installed:
    pip install windows-curses

'''

import curses
import random

def main(stdscr) -> None:
    '''
    Initialize the game window and handle the main game loop.
    '''
    # Initial setup
    stdscr.clear()  # Clear the screen
    curses.curs_set(0)  # Hide the cursor

    sh, sw = stdscr.getmaxyx()  # Terminal height and width
    w = curses.newwin(sh, sw, 0, 0)  # Create a new full-screen window
    w.keypad(1)  # Enable arrow keys
    w.timeout(100)  # Refresh every 100ms

    # Initial snake and food setup
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]
    food = [random.randint(10, sh - 2), random.randint(10, sw - 2)]
    w.addch(food[0], food[1], curses.ACS_PI) # Food character "π"

    # Initial direction
    key = curses.KEY_RIGHT

    # Main game loop
    while True:
        # Draw the snake
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Calculate new head
        head = snake[0].copy()
        if key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1

        # Collision checks
        if (
            head in snake or
            head[0] in [0, sh] or
            head[1] in [0, sw]
        ):
            msg = "Game Over! Press any key to exit..."
            w.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            w.refresh()
            w.getch()
            break

        # Insert new head
        snake.insert(0, head)

        # Check for food
        if head == food:
            food = None
            while food is None:
                nf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(head[0], head[1], curses.ACS_CKBOARD)

# Run the game in a curses wrapper to handle cleanup
if __name__ == "__main__":
    # Initialize the curses application
    # and call the main function to start the game.
    curses.wrapper(main)
