'''
A small maze generator using a random walk algorithm.
(Testing purposes only)
'''
import random

# This code generates a maze using a random walk algorithm.
maze_size = 11  # Size of the maze (must be odd)
# Initialize the array with all zeros
array = [[0 for _ in range(maze_size)] for _ in range(maze_size)]

# Set 0st and maze_size - 2th columns (index 0 and maze_size - 2) for all rows
for row in range(1,maze_size - 1):
    for col in range(1, maze_size - 1):
        if col % 2 == 1 and row % 2 == 1:  # Only set odd rows and columns to 1
            array[row][col] = 1

# Optional: print the array
for row in array:
    print(row)

# randlomly choose a "1" cell in the row or column closed to "edge"
# and mark it as "starting" point
row_candidate = [(1, col) for col in range(1, maze_size - 1, 2)] + [(maze_size - 2, col) for col in range(1, maze_size - 1, 2)]

col_candidate = [(row, 1) for row in range(1, maze_size - 1, 2)] + [(row, maze_size - 2) for row in range(1, maze_size - 1, 2)]

all_candidate = row_candidate + col_candidate

unique_candidate = list(set(all_candidate))

start = random.choice(unique_candidate)

print("start:", start)

# Mark the starting point in the array
array[start[0]][start[1]] = 2   # 2 represents the starting point
# Optional: print the array with the starting point
for row in array:
    print(row)

# From start point, randomly choose a direction (up, down, left, right) and mark the next cell as "1"
# if it is "0" and not already visited (not "2") and not the first or last row/column
directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # right, left, down, up

visited = set()  # Set to keep track of visited cells in order to avoid duplicates
visited.add(start)  # Mark the starting point as visited


# Start from the starting point and randomly choose a direction
current = start  # Start from the starting point

# Until "1" cells are visited except the starting point
valid_directions = directions.copy()  # List to store valid directions

num_ones = sum(row.count(1) for row in array)

while len(visited) <= num_ones:

    current_direction = random.choice(valid_directions)  # Randomly choose a direction

    new_row = current[0] + current_direction[0]
    new_col = current[1] + current_direction[1]

    # Check if the new position is valid and not visited
    if (1 <= new_row < maze_size ) and (1 <= new_col < maze_size ) and (array[new_row][new_col] == 1):
        array[new_row][new_col] = 2  # Mark as visited
        # Mark the cell between the current and new position as "1"
        array[current[0] + current_direction[0] // 2][current[1] + current_direction[1] // 2] = 2
        visited.add((new_row, new_col))  # Add to visited set
        current = (new_row, new_col)  # Update current position
        # Optional: print the array with the visited cell
        print()
        print("========================")
        print(visited)
        for row in array:
            print(row)
        print("========================")
        #break  # Break out of the loop after marking one cell
    else:
        # if the new position is not valid, continue to the next direction
        valid_directions.remove(current_direction)
        # Check if there are any valid directions left
        if valid_directions:
            current_direction = random.choice(valid_directions)
        else:
            # If no valid directions left, go back to the previous cell
            # and repeat the process until all cells are visited
            # This part is not implemented in this code snippet
            current = random.choice(list(visited))  # Randomly choose a visited cell
            valid_directions = directions.copy()  # Reset valid directions
            # Continue the process from the new current position


# Randomly choose a cell from the unique candifates array and is not the starting point and mark it as the end point
end_candidate = [cell for cell in unique_candidate if cell != start]

# find out the the longest cell in the unique candidate array from the starting point and through the visited cells
# and mark it as the end point
end = max(end_candidate, key=lambda cell: abs(cell[0] - start[0]) + abs(cell[1] - start[1]))

array[end[0]][end[1]] = 4 # Mark as ending point

array[start[0]][start[1]] = 3 # Mark as starting point

# Optional: print the array with the visited cells
print()
print("========================")
print("Final array with visited cells:")
print("Starting point:", start)
print("Ending point:", end)
print("Visited cells:", len(visited))
print(visited)
print("Final array:")
for row in array:
    print(row)
print("========================")
