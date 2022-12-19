"""
Advent of Code 2022 - Day 14
https://adventofcode.com/2022/day/14

-- Sand pouring in from 500,0
-- sand one unit at a time
-- next sand comes after previous comes to rest
-- sand moves down, down-left, down-right in order of preference
-- how many units of sand come to rest before next sand goes into the abyss
-- units of time don't matter

-- Approach
-- First step - create lines of rock

"""

#from ast import literal_eval
#import numpy
import itertools

#FILE_PATH = "day_14/input.txt"
FILE_PATH = "day_14/test.txt"

def print_grid(grid, x_min, x_max, y_min, y_max):
    '''
    doc string here
    '''

    print(x_min, x_max, y_min, y_max)

    grid_subset = grid[y_min:y_max + 1]

    for line in grid_subset:
        print("".join(line[x_min:x_max + 1]))

def main():
    '''
    doc string here
    '''
    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()
        #text_data = text_data.split('\n\n')
        #text_data = [line.splitlines() for line in text_data]
        #print(len(text_data))
        #print(text_data[0])
        text_data = [line.split("->") for line in text_data]
        text_data = [[item.replace(' ','') for item in line] for line in text_data]
        text_data = [[item.split(',') for item in line] for line in text_data]
        data = [[(int(a), int(b)) for (a,b) in line] for line in text_data]

        # Need a way to track which positions have rock
        # Create a matrix?
        # What are the dimensions?
        # Just add 100 each side for now
        x_pos_list = [[pos_x for (pos_x, pos_y) in line] for line in data]
        x_pos_list = list(itertools.chain(*x_pos_list))
        x_max = max(x_pos_list)
        x_min = min(x_pos_list)

        y_pos_list = [[pos_y for (pos_x, pos_y) in line] for line in data]
        y_pos_list = list(itertools.chain(*y_pos_list))
        y_max = max(y_pos_list)
        y_min = min(y_pos_list)


        # https://stackoverflow.com/questions/72128627/how-to-assign-a-value-to-nested-list-while-keeping-the-original-list-in-python
        grid = [['.' for _ in range(x_max + 100)] for _ in range(y_max+100)]
        #print_grid(grid, max(x_min - 10, 0), x_max + 10, max(y_min - 10, 0), y_max + 10)

        # Iterate over every line, and then every tuple
        for line in data:
            for i in range(len(line) - 1):
                #grid[line[i][1]][line[i][0]] = '#'
                # If horizontal line
                if line[i][1] == line[i+1][1]:
                    # Get min x coord
                    line_x_min = min(line[i][0], line[i+1][0])
                    line_x_max = max(line[i][0], line[i+1][0])
                    # Get max x coord
                    for j in range(line_x_min, line_x_max + 1):
                        #print(line[i][0], j)
                        grid[line[i][1]][j] = '#'
                # If vertical line
                elif line[i][0] == line[i+1][0]:
                    # Get min y coord
                    line_y_min = min(line[i][1], line[i+1][1])
                    line_y_max = max(line[i][1], line[i+1][1])
                    # Get max x coord
                    for j in range(line_y_min, line_y_max + 1):
                        #print(line[i][0], j)
                        grid[j][line[i][0]] = '#'
        
        print_grid(grid, max(x_min - 10, 0), x_max + 10, max(y_min - 10, 0), y_max + 10)

        # Now drop sand

        



if __name__ == "__main__":
    main()
