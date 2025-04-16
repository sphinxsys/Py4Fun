'''
A python script to generate a maze using a recursive backtracking algorithm.
The maze is represented as a 2D grid, where walls are removed to create paths. 
The script also includes a function to display the maze using Pygame.
'''

import random
import pygame
import sys
from typing import List, Tuple

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Directions for moving in the maze (up, down, left, right)
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
font = pygame.font.SysFont('arial', 24)

clock = pygame.time.Clock()
pygame.display.set_caption("Maze Generator")
screen.fill(WHITE)
pygame.display.flip()
pygame.time.delay(1000)


def draw_block(color: Tuple[int, int, int], position: Tuple[int, int]) -> None:
    '''
    Draw a block on the screen at the given position.
    '''
    rect = pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, rect)
    
# initialize a array to store the maze. 
# 0 represents a wall, 1 represents a path.
# For example, a 19 x 18 maze will look like this:
#        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
#        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#

# The maze is generated using a recursive backtracking algorithm.
# The algorithm starts from a random "1" cell closing to edge, mark it as the 
# "starting" point and randomly visits its neighbors (up down left right) and 
# removes the wall "0" between the current cell and the neighbor "1" cell if 
# the neighbor is not visited yet. The algorithm continues until all cells are 
# visited. And then choose a random "1" cell closing to the edge as the "ending"
# point.

# initialize a array like above
maze = [[0 for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]
# set the edge cells to 1
for i in range(WIDTH // BLOCK_SIZE):
    maze[0][i] = 1
    maze[HEIGHT // BLOCK_SIZE - 1][i] = 1
for i in range(HEIGHT // BLOCK_SIZE):
    maze[i][0] = 1
    maze[i][WIDTH // BLOCK_SIZE - 1] = 1

# display the maze
def display_maze(maze: List[List[int]]) -> None:
    '''
    Display the maze on the screen.
    '''
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_block(GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE))
            else:
                draw_block(WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE))

    pygame.display.flip()
    pygame.time.delay(1000)


display_maze(maze)