"""
Advent of Code 2022 - Day 9

- rope with head and tail
- head and tail must always be touching (overlapping or diagonally adjacent is
- fine)
- if head is two steps up, down, left, right, then tail will move towards head
- if head and tail are not touching, and not in same row or column, then will
- move diagonally to keep up
- head and tail start overlapping

- take moves from the input file
- do each move step by step
- keep track of tail position
- work out how many positions the tail visited

- assume that no fixed grid

- approach
- keep a list of positions visited by the tail 
    - list of tuples
- take each line, and perform the moves one by one
- so keep iterating until move count is 0
- variable for head and tail position which is a tuple
- how do i move the tail?
- start off by updating the head position

"""

FILE_PATH = "day_9/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()
    print(text_data[0:5])
    print(len(text_data))

    text_data = [line.split() for line in text_data]
    moves = [[dir, int(count)] for [dir, count] in text_data]
    print(moves[0:5])

    h_pos = [0,0]
    t_pos = [0,0]
    t_visited = []

    for [dir, count] in moves:
        for i in range(count):
            if dir == "U":
                h_pos[1] += 1
            elif dir == "D":
                h_pos[1] -= 1
            elif dir == "L":
                h_pos[0] -= 1
            elif dir == "R":
                h_pos[0] += 1
            else:
                print("invalid direction")
                break
            
            # this is incorrect, only move if not overlapping or touching
            # so each axis has a max difference of two
            if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
                # enumerate scenarios
                # same column but different row, then move one direction towards row
                if (h_pos[0] == t_pos[0]):
                    t_pos[1] += (h_pos[1] - t_pos[1]) / abs(h_pos[1] - t_pos[1])
                # same column but different row, then move one direction towards row
                elif (h_pos[1] == t_pos[1]):
                    t_pos[0] += (h_pos[0] - t_pos[0]) / abs(h_pos[0] - t_pos[0])
                # same column but different row, then move one direction towards row
                else:
                    t_pos[0] += (h_pos[0] - t_pos[0]) / abs(h_pos[0] - t_pos[0])
                    t_pos[1] += (h_pos[1] - t_pos[1]) / abs(h_pos[1] - t_pos[1])

            print(h_pos, t_pos)
            t_visited.append(tuple(t_pos))

    print(len(set(t_visited)))

