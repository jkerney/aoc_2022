"""
Advent of Code 2022 - Day 9
"""

FILE_PATH = "day_9/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()
    #print(text_data[0:5])
    #print(len(text_data))

    text_data = [line.split() for line in text_data]
    moves = [[dir, int(count)] for [dir, count] in text_data]
    #print(moves[0:5])

    h_pos = [0,0]
    t_pos = [0,0]
    t_visited = []

    for [direction, count] in moves:
        for i in range(count):
            if direction == "U":
                h_pos[1] += 1
            elif direction == "D":
                h_pos[1] -= 1
            elif direction == "L":
                h_pos[0] -= 1
            elif direction == "R":
                h_pos[0] += 1
            else:
                print("invalid direction")
                break

            # move tail if difference in x or y axis is greater than 1
            if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
                # same column but different row, then move one direction towards row
                if h_pos[0] == t_pos[0]:
                    t_pos[1] += (h_pos[1] - t_pos[1]) / abs(h_pos[1] - t_pos[1])
                # same row but different column, then move one direction towards column
                elif h_pos[1] == t_pos[1]:
                    t_pos[0] += (h_pos[0] - t_pos[0]) / abs(h_pos[0] - t_pos[0])
                # neither, then need to make a diagonal move
                else:
                    t_pos[0] += (h_pos[0] - t_pos[0]) / abs(h_pos[0] - t_pos[0])
                    t_pos[1] += (h_pos[1] - t_pos[1]) / abs(h_pos[1] - t_pos[1])

            #print(h_pos, t_pos)
            t_visited.append(tuple(t_pos))

    print(len(set(t_visited)))
