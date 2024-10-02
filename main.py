import time
import os
import random
import sys

def create_initial_grid(rows, cols):

    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            if random.randint(0, 7) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid

def print_grid(rows, cols, grid, generation):
    clear_console()

    output_str = ""

    output_str += "Generation {0} - To exit the program press <Ctrl-C>\n\r".format(generation)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += ". "
            else:
                output_str += "@ "
        output_str += "\n\r"
    print(output_str, end=" ")
    
def create_next_grid(rows, cols, grid, next_grid):


    for row in range(rows):
        for col in range(cols):
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)

            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            else:
                next_grid[row][col] = grid[row][col]
                
def get_live_neighbors(row, col, rows, cols, grid):

    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life_sum += grid[((row + i) % rows)][((col + j) % cols)]
    return life_sum

def grid_changing(rows, cols, grid, next_grid):

    for row in range(rows):
        for col in range(cols):
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False

