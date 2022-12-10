"""
Advent of Code 2022 - Day 1

Task 1:
Input file is a text file
Each row is the amount of calories in an item carried by an elf
A blank space indicates a new elf
Add up the calories for each elf
Find the maximum amount of calories carried by an elf

Task 2:
Find the sum of calories carried by the top 3 elves
"""

FILE_PATH = "day_1/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    # Split the string by the blank lines
    # Each element in this list is an elf
    text_data = text_data.split('\n\n')
    # For each elf, split the string into individual calroie counts
    text_data = [line.splitlines() for line in text_data]
    elf_data = [map(int, elf) for elf in text_data]
    elf_data = [sum(elf) for elf in elf_data]

    # Task 1
    print(max(elf_data))

    # Task 2
    elf_data.sort(reverse=True)
    print(sum(elf_data[:3]))
