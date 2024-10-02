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

