'''
Advent of Code 2022 - Day 3 Part 1
'''

#FILE_PATH = "day_3/test.txt"
FILE_PATH = "day_3/input.txt"

def main():
    '''
    Solve AoC 2022 Day 3 Part 1
    '''

    with(open(FILE_PATH, 'r', encoding="utf-8")) as input_file:

        data = input_file.read()
        data = data.splitlines()
        data = [[x[0:int(len(x)/2)], x[int(len(x)/2):len(x)]] for x in data]

        # Find common characters in each rucksack
        common_chars = []
        for sack in data:
            unique_char = set(sack[0])
            for char in unique_char:
                if char in sack[1]:
                    common_chars.append(char)

        # Turn common_chars into priority number
        priority = []

        for char in common_chars:
            if char.islower():
                priority.append(ord(char) - 96)
            else:
                priority.append(ord(char) - 38)

        print(sum(priority))

if __name__ == '__main__':
    main()
