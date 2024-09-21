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

