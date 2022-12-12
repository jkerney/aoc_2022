"""
Advent of Code 2022 - Day 12

- input is height map
- a is lowest, z is highest
- S current position, elevation a
- E best signal, elevation z

- Reach E in as few steps as possible
- can move up, down, left, right
- can move to a square of at most one higher elevation
- find the shortest path to E

- Approach 
- Start with a simple approach that gets an answer
- Then move to an optimal solution

- Can choose best option each spot, but what if you 
- get stuck? Then you need to backtrack

- Step 1, replace every letter with a number
- tuple for start point
- tuple for end point

- is this shortest path?
- create a graph of connected points.
- then use a shortest path algorithm
- give each node a name based on its position
- then add edge to the network


"""

#import math
import networkx as nx

FILE_PATH = "day_12/input.txt"
#FILE_PATH = "day_12/test.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()

    x_len = len(text_data[0])
    y_len = len(text_data)

    text_data = [[letter for letter in x] for x in text_data]

    # Get the start and end points, then change to their heigh
    for x in range(x_len):
        for y in range(y_len):

            if text_data[y][x] == 'S':
                start_pos = (x,y)
                text_data[y][x] = 'a'
            elif text_data[y][x] == 'E':
                end_pos = (x,y)
                text_data[y][x] = 'z'

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

    # Find the shortest path
    path = nx.shortest_path(G, start_pos, end_pos)
    print(len(path) - 1)

