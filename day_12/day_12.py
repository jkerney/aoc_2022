"""
Advent of Code 2022 - Day 12
https://adventofcode.com/2020/day/12
"""

#import math
import networkx as nx

FILE_PATH = "day_12/input.txt"
#FILE_PATH = "day_12/test.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()

    # Get dimensions of grid
    x_len = len(text_data[0])
    y_len = len(text_data)

    # Turn into list of lists (each element a single letter)
    text_data = [[letter for letter in x] for x in text_data]

    # Get the start and end points, then change to their actual height
    for x in range(x_len):
        for y in range(y_len):

            if text_data[y][x] == 'S':
                start_pos = (x,y)
                text_data[y][x] = 'a'
            elif text_data[y][x] == 'E':
                end_pos = (x,y)
                text_data[y][x] = 'z'

    # Turn letters into ordered numbers
    grid = [[ord(letter) for letter in x] for x in text_data]

    G=nx.DiGraph()

    # Add possible paths as edges to a directed graph
    for x in range(x_len):
        for y in range(y_len):
            # add path above
            if y > 0 and grid[y-1][x] <= (grid[y][x] + 1):
                G.add_edge((x,y), (x,y-1))
            # add path below
            if y < y_len - 1 and grid[y+1][x] <= (grid[y][x] + 1):
                G.add_edge((x,y), (x,y+1))
            # add path left
            if x > 0 and grid[y][x-1] <= (grid[y][x] + 1):
                G.add_edge((x,y), (x-1,y))
            # add path right
            if x < x_len - 1 and grid[y][x+1] <= (grid[y][x] + 1):
                G.add_edge((x,y), (x+1,y))

    # Part 1 - Find the shortest path from S to E
    path = nx.shortest_path(G, start_pos, end_pos)
    print(len(path) - 1)

    # Part 2 - find length of all shortest paths
    # starting at 'a'. Find the min length of these
    # shortest paths

    start_pos_list = [start_pos]

    # Add start points of grid points with 'a'
    for x in range(x_len):
        for y in range(y_len):
            if text_data[y][x] == 'a':
                start_pos_list.append((x,y))

    # Calc all shortest paths and add to list
    shortest_path_lengths = []
    for coord in start_pos_list:
        try:
            path = nx.shortest_path(G, coord, end_pos)
            shortest_path_lengths.append(len(path) - 1)
        except:
            pass

    print(min(shortest_path_lengths))
