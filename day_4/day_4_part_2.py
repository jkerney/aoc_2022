'''
Advent of Code 2019 - Day 4 - Part 2
'''

#FILE_PATH = "day_4/test.txt"
FILE_PATH = "day_4/input.txt"

def main():
    '''
    Implement solution to AoC - day 4 part 2
    '''

    with(open(FILE_PATH, 'r', encoding='utf-8')) as file:

        data = file.read()
        data = data.splitlines()
        data = [line.split(',') for line in data]
        data = [[x.split('-') for x in line] for line in data]
        data = [[(int(pair[0]), int(pair[1])) for pair in line]
                for line in data]

        # Each element in data is a pair of tuples
        # Each tuple is a range of numbers
        # Iterate over the pairs of tuples
        # We need to check if there's any overlap in the range of the tuples
        # Conditions to check
        # 1. One tuple contains the other
        # 2. The start of the first tuple is within the range of the second
        # 3. The end of the first tuple is within the range of the second
        counter = 0

        for pair in data:
            # Check if the second tuple contains the first
            if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
                counter += 1
            # Check if the first tuple contains the second
            elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
                counter += 1
            # Check if the first tuple start is within the range of the second
            elif pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
                counter += 1
            # Check if the first tuple end is within the range of the second
            elif pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]:
                counter += 1

        print(counter)

if __name__ == "__main__":
    main()
