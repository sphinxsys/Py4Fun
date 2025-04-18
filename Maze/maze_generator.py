'''
This code generates a maze using a random walk algorithm.
In the latest version, the maze is generated using a recursive backtracking algorithm.
The maze is represented as a 2D grid, where walls are removed to create paths. 
'''

import random
from typing import List, Tuple

import pygame

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
ORANGE_WALL = (255, 165, 0)

# Directions for moving in the maze (right, left, down, up)
DIRS = [(0, 2), (0, -2), (2, 0), (-2, 0)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
font = pygame.font.SysFont('arial', 24)
clock = pygame.time.Clock()

screen.fill(WHITE)


def draw_block(color: Tuple[int, int, int], position: Tuple[int, int]) -> None:
    '''
    Draw a block on the screen at the given position.
    '''
    rect = pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, rect)


def draw_maze(maze_array: List[List[int]]) -> None:
    '''
    Draw the maze on the screen.

    input:
        maze_array: The maze array to be drawn.
    output:
        None
    '''
    for r, _row in enumerate(maze_array):
        for c, cell in enumerate(_row):
            pos = (c * BLOCK_SIZE, r * BLOCK_SIZE)
            if cell == 0:
                draw_block(ORANGE_WALL, pos)  # Wall
            elif cell == 2:
                draw_block(GREEN, pos) # Starting point
            elif cell == 3:
                draw_block(GRAY, pos)  # Visited path
            elif cell == 4:
                draw_block(BLACK, pos)  # Ending point
            else:
                draw_block(WHITE, pos) # Available path

    pygame.display.flip()
    clock.tick(FPS)

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

# This code generates a maze using a random walk algorithm.
MAZE_ROW_SIZE = 29  # Size of the maze (must be odd)
MAZE_COL_SIZE = 39  # Size of the maze (must be odd)

def initialize_maze_array(maze_row_size: int, maze_col_size: int) -> List[List[int]]:
    """
    Initialize the maze array with walls (0) and paths (1).
    Only odd rows and columns are set to 1 to create the grid structure.

    input:
        maze_row_size: The number of rows in the maze.
        maze_col_size: The number of columns in the maze.
    output:
        maze_array: A 2D list representing the maze, where 0 is a wall and 1 is a path.
    """
    maze_array = [[0 for _ in range(maze_col_size)] for _ in range(maze_row_size)]
    for row in range(1, maze_row_size - 1):
        for col in range(1, maze_col_size - 1):
            if col % 2 == 1 and row % 2 == 1:  # Only set odd rows and columns to 1
                maze_array[row][col] = 1
    return maze_array

def choose_point(maze_array: List[List[int]],
                 is_starting_point: bool = True) -> Tuple[Tuple[int, int]]:
    """
    Randomly choose a "1" cell in the row or column close to the "edge"
    and mark it as the "starting" point or "ending" point.
    The starting point is marked as "2" and the ending point is marked as "4".

    input:
        maze_array: The maze array to be generated.
        is_starting_point: A boolean value to indicate if the point is the starting point.

    output:
        point: A tuple representing the coordinates of the chosen point in the maze.

    """
    row_size = len(maze_array)
    col_size = len(maze_array[0])

    row_candidate = [(1, col) for col in range(1, col_size - 1, 2)] + \
        [(row_size - 2, col) for col in range(1, col_size - 1, 2)]
    col_candidate = [(row, 1) for row in range(1, row_size - 1, 2)] + \
        [(row, col_size - 2) for row in range(1, row_size - 1, 2)]

    all_candidate = row_candidate + col_candidate
    unique_candidate = list(set(all_candidate))
    if not is_starting_point:
        # exclude the starting point from the candidates by the value of the cell
        # in the array
        unique_candidate = [point for point in unique_candidate if point != 2]

    point = random.choice(unique_candidate)

    return point


def generate_maze(maze_array: List[List[int]],
                  visited_path: List[Tuple[int, int]],
                  current_point: Tuple[int, int]) -> Tuple[List[List[int]],
                                               List[Tuple[int, int]],
                                               Tuple[int, int]]:
    """
    Generate a maze using a recursive backtracking algorithm.
    The algorithm starts from the current position and randomly visits its neighbors.
    It removes the wall between the current cell and the neighbor cell if the neighbor
    is not visited yet.
    The algorithm continues until all cells are visited.

    input:
        maze_array: The maze array to be generated.
        visited_path: The list of visited cells.
        current_point: The current position in the maze.

    output:
        maze_array: The updated maze array.
        visited_path: The updated list of visited cells.
        current_point: The updated current position in the maze.
    """
    valid_directions = DIRS.copy()  # Reset valid directions

    while len(valid_directions) > 0:
        current_direction = random.choice(valid_directions)  # Randomly choose a direction
        new_row = current_point[0] + current_direction[0]
        new_col = current_point[1] + current_direction[1]

        # Check if the new position is valid and not visited
        if (1 <= new_row < MAZE_ROW_SIZE) and \
             (1 <= new_col < MAZE_COL_SIZE) and \
             (maze[new_row][new_col] == 1):
            maze_array[new_row][new_col] = 3  # Mark as visited path (3)
            # Mark the cell between the current and new position as "3" (path)
            maze_array[current_point[0] + current_direction[0] // 2] \
                      [current_point[1] + current_direction[1] // 2] = 3
            visited_path.append((new_row, new_col))  # Add to visited set
            current_point = (new_row, new_col)  # Update current position
            break

        # If the new position is not valid, continue to the next direction
        valid_directions.remove(current_direction)
        if len(valid_directions) == 0:
            # If no valid directions left, randomly choose a visited cell
            # and mark it as the current position (random walk algorithm)
            # current = random.choice(list(visited))

            # instead of randomly choosing a visited cell, we can take the previous
            # visited cell as the current position to avoid hard to find the new
            # current point (backtracking algorithm)
            if len(visited_path) > 0:
                current_point = visited_path.pop()  # Pop a visited cell to backtrack

    return maze_array, visited_path, current_point

# Initialize a maze array to store the maze
maze = initialize_maze_array(MAZE_ROW_SIZE, MAZE_COL_SIZE)

# the number of "1" cells in the array
num_ones = sum(row.count(1) for row in maze)

# Set to keep track of visited cells in order to avoid duplicates
visited = []

# Mark the starting point in the array
current = (1, 1)  # Current position in the maze

# display this array using pygame
RUNNING = True

# Animation loop
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    if len(visited) == 0:
        # Mark the starting point in the array
        start = choose_point(maze)
        maze[start[0]][start[1]] = 2  # 2 represents the starting point

        visited.append(start)  # Mark the starting point as visited

        # Start from the starting point and randomly choose a direction
        current = start  # Start from the starting point

        # Draw the array with the starting point
        draw_maze(maze)

    while num_ones > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        maze, visited, current = generate_maze(maze, visited, current)
        num_ones = sum(row.count(1) for row in maze)
        draw_maze(maze)

    if not any(4 in row for row in maze):
        # Mark the ending point in the array
        end = choose_point(maze, False)
        maze[end[0]][end[1]] = 4  # 4 represents the ending point
        draw_maze(maze)

        # Finally break the wall outside of the starting point and ending point
        if start[0] == 1:
            maze[0][start[1]] = 3
        elif start[0] == MAZE_ROW_SIZE - 2:
            maze[MAZE_ROW_SIZE - 1][start[1]] = 3
        elif start[1] == 1:
            maze[start[0]][0] = 3
        else:
            maze[start[0]][MAZE_COL_SIZE - 1] = 3

        if end[0] == 1:
            maze[0][end[1]] = 3
        elif end[0] == MAZE_ROW_SIZE - 2:
            maze[MAZE_ROW_SIZE - 1][end[1]] = 3
        elif end[1] == 1:
            maze[end[0]][0] = 3
        else:
            maze[end[0]][MAZE_COL_SIZE - 1] = 3

        draw_maze(maze)

pygame.quit()
