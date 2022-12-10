"""
Advent of Code 2022 - Day 10
"""

FILE_PATH = "day_10/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()

    # Part 1
    reg_x = [1]

    for line in text_data:
        if line == "noop":
            reg_x.append(reg_x[-1])
        elif line.startswith("addx"):
            reg_x.append(reg_x[-1])
            reg_x.append(reg_x[-1] + int(line[5:]))

    sig_strength = [
        x*y for x, y in zip(reg_x,
                            list(range(1,len(reg_x)+1)))
    ]

    indices = [19, 59, 99, 139, 179, 219]
    result = sum([sig_strength[i] for i in indices])
    print(result)

    # Part 2
    # Get the horizontal position of the CRT at each cycle
    hor_pos = list(range(0,40)) * 6
    # Get the difference between CRT position and register X
    sprite_rel = [x - y for x, y in zip(reg_x, hor_pos)]
    screen_output = ["#" if x in range(-1,2) else "." for x in sprite_rel]
    screen_output_str = "".join(screen_output)

    for i in range(0,6):
        print(screen_output_str[i*40:(i+1)*40])
