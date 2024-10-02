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

    output_str += "Geração/Generation {0} - Para sair do programa pressione <Ctrl-c> / To exit the program press <Ctrl-C>\n\r".format(generation)
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

def get_integer_value(prompt, low, high):

    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Imput não é um valor integral válido / Input was not a valid integer value.")
            continue
        if value < low or value > high:
            print("Imput não está dentro dos limites valor <= {0} ou valor >= {1}/ Input was not inside the bounds (value <= {0} or value >= {1}).".format(low, high))
        else:
            break
    return value


def run_game():

    clear_console()

    rows = get_integer_value("Insira o número de linhas / Enter the number of rows (10-60): ", 10, 60)
    clear_console()
    cols = get_integer_value("Insira o número de colunas / Enter the number of cols (10-118): ", 10, 118)

    generations = 5000
    resize_console(rows, cols)

    current_generation = create_initial_grid(rows, cols)
    next_generation = create_initial_grid(rows, cols)

    gen = 1
    for gen in range(1, generations + 1):
        if not grid_changing(rows, cols, current_generation, next_generation):
            break
        print_grid(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(1 / 5.0)
        current_generation, next_generation = next_generation, current_generation

    print_grid(rows, cols, current_generation, gen)
    return input("<Enter> para sair ou r para começar de novo / <Enter> to exit or r to run again: ")


run = "r"
while run == "r":
    out = run_game()
    run = out

