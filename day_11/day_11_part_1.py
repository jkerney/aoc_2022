"""
Advent of Code 2022 - Day 11 - Part 1
"""

import math

FILE_PATH = "day_11/input.txt"
#FILE_PATH = "day_11/test.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.split('\n\n')
    count = len(text_data)
    text_data = [line.splitlines() for line in text_data]

    # Get items worry levels
    worry = [line[1].split()[2:] for line in text_data]
    worry = [[int(x.rstrip(',')) for x in line] for line in worry]

    # Get operation type
    op_type = [line[2].split()[4] for line in text_data]

    # Get operand
    operand = [line[2].split()[5] for line in text_data]

    # test divisible amount
    test_div = [line[3].split()[3] for line in text_data]

    # monkey to throw to if true
    true_monkey = [line[4].split()[5] for line in text_data]
    false_monkey = [line[5].split()[5] for line in text_data]

    inspect_count = [0] * count

    # Now iterate through a round
    for i in range(500):
        # iterate through monkeys
        #print(worry)
        for j in range(count):
            inspect_count[j] += len(worry[j])
            # get new worry level
            if op_type[j] == '+':
                worry[j] = [x + int(operand[j]) for x in worry[j]]
            elif op_type[j] == '*' and operand[j] == 'old':
                worry[j] = [x * x for x in worry[j]]
            elif op_type[j] == '*':
                worry[j] = [x * int(operand[j]) for x in worry[j]]

            worry[j] = [math.floor(x/3) for x in worry[j]]

            # throw to other monkeys
            for k in range(len(worry[j])):
                if worry[j][k] % int(test_div[j]) == 0:
                    worry[int(true_monkey[j])].append(worry[j][k])
                else:
                    worry[int(false_monkey[j])].append(worry[j][k])
            worry[j] = []

        #print(worry)
        #print(inspect_count)

    inspect_count.sort(reverse=True)
    print(inspect_count)
    print(inspect_count[0] * inspect_count[1])
