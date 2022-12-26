'''
Advent of Code 2022 - Day 3 Part 2
'''

#FILE_PATH = "day_3/test.txt"
FILE_PATH = "day_3/input.txt"

def main():
    '''
    Solve AoC 2022 Day 3 Part 2
    '''

    with(open(FILE_PATH, 'r', encoding="utf-8")) as input_file:

        data = input_file.read()
        data = data.splitlines()

        # Create a list where each element
        # is a list of three strings
        data = [data[i:i+3] for i in range(0, len(data), 3)]

        # Now iterate over every list in data
        # Turn the first list into a set of unique chars
        # Then iterate over unique chars and check if it's also in second and
        # third lists.
        # If it is, add it to common_chars
        common_chars = []

        for group in data:
            unique_char = set(group[0])
            for char in unique_char:
                if char in group[1] and char in group[2]:
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
