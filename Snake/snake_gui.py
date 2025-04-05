'''
    Simple Snake Game using Pygame
'''

import random
import sys

import pygame

# Initialize Pygame
pygame.init()  # type: ignore

# Game settings
WIDTH, HEIGHT = 800, 500
BLOCK_SIZE = 20
FPS = 5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Font
font = pygame.font.SysFont('arial', 24)

def draw_block(color, position):
    ''''
    Draw a block on the screen at the given position.'
    '''
    rect = pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, rect)

def random_food():
    '''
    Generate random food position within the screen bounds.
    '''
    x = random.randint(1, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(1, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return x, y

def show_text(text, color, center):
    '''
    Display text on the screen at the given center position.
    '''
    label = font.render(text, True, color)
    screen.blit(label, label.get_rect(center=center))


def main():
    '''
       Main function to run the game.
    '''
    # Initialize game variables
    clock = pygame.time.Clock()
    snake = [(100, 100)]
    direction = (BLOCK_SIZE, 0)
    food = random_food()
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        # Move snake
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Game over conditions
        if (
            new_head in snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            screen.fill(BLACK)
            show_text("Game Over! Press any key to exit", RED, (WIDTH//2, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(500)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                        pygame.quit()
                        sys.exit()

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        for block in snake:
            draw_block(GREEN, block)
        draw_block(RED, food)
        show_text(f"Score: {score}", WHITE, (60, 20))

        pygame.display.flip()

# Main entry point
if __name__ == "__main__":
    main()
