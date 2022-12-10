"""
Advent of Code 2022 - Day 10
"""

FILE_PATH = "day_10/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()

    # Calculate register X value at each cycle
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
    