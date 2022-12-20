"""
Advent of Code 2022 - Day 14 Part 1
https://adventofcode.com/2022/day/14
"""

#from ast import literal_eval
#import numpy
import itertools

FILE_PATH = "day_14/input.txt"
#FILE_PATH = "day_14/test.txt"

def print_grid(grid, x_min, x_max, y_min, y_max):
    '''
    Helper function to print grid of rocks and sand
    '''

    print(x_min, x_max, y_min, y_max)
    grid_subset = grid[y_min:y_max + 1]

    for line in grid_subset:
        print("".join(line[x_min:x_max + 1]))

def main():
    '''
    Day 14 Part 1 - calculate count of sand that has come to rest
    before it hits the abyss
    '''
    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()

        text_data = [line.split("->") for line in text_data]
        text_data = [[item.replace(' ','') for item in line] for line in text_data]
        text_data = [[item.split(',') for item in line] for line in text_data]
        data = [[(int(a), int(b)) for (a,b) in line] for line in text_data]

        # Get max and min x and y coords for rocks
        x_pos_list = [[pos_x for (pos_x, pos_y) in line] for line in data]
        x_pos_list = list(itertools.chain(*x_pos_list))
        x_max = max(x_pos_list)
        x_min = min(x_pos_list)

        y_pos_list = [[pos_y for (pos_x, pos_y) in line] for line in data]
        y_pos_list = list(itertools.chain(*y_pos_list))
        y_max = max(y_pos_list)
        y_min = min(y_pos_list)

        # Create grid
        # https://stackoverflow.com/questions/72128627/how-to-assign-a-value-to-nested-list-while-keeping-the-original-list-in-python
        grid = [['.' for _ in range(x_max + 100)] for _ in range(y_max+100)]

        # Insert a '#' for each position of rock
        for line in data:
            for i in range(len(line) - 1):
                # If horizontal line
                if line[i][1] == line[i+1][1]:
                    # Get min and max of x coord of line
                    line_x_min = min(line[i][0], line[i+1][0])
                    line_x_max = max(line[i][0], line[i+1][0])
                    for j in range(line_x_min, line_x_max + 1):
                        grid[line[i][1]][j] = '#'
                # If vertical line
                elif line[i][0] == line[i+1][0]:
                    # Get min and max y coord of line
                    line_y_min = min(line[i][1], line[i+1][1])
                    line_y_max = max(line[i][1], line[i+1][1])
                    for j in range(line_y_min, line_y_max + 1):
                        grid[j][line[i][0]] = '#'

        print_grid(grid, max(x_min - 10, 0), x_max + 10, max(y_min - 10, 0), y_max + 10)

        # Now drop sand until one of them hits the abyss
        hit_abyss = False
        count_sand_rest = 0

        while hit_abyss is False:
            #print("New sand")
            sand_pos = (500, -1)

            while True:

                old_sand_pos = sand_pos
                # Check if sand is going to hit abyss
                if sand_pos[1] > y_max:
                    hit_abyss = True
                    break
                # Check if sand can move down
                elif grid[sand_pos[1] + 1][sand_pos[0]] == '.':
                    sand_pos = (sand_pos[0], sand_pos[1] + 1)
                # Check if sand can move down-left
                elif grid[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
                    sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
                # Check if sand can move down-right
                elif grid[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
                    sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
                # Otherwise sand has come to rest
                else:
                    count_sand_rest += 1
                    break

                # Update position of the sand
                grid[old_sand_pos[1]][old_sand_pos[0]] = '.'
                grid[sand_pos[1]][sand_pos[0]] = 'o'

        print_grid(grid, max(x_min - 10, 0), x_max + 10, max(y_min - 10, 0), y_max + 10)
        print(count_sand_rest)

if __name__ == "__main__":
    main()
