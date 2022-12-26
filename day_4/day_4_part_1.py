'''
Advent of Code 2019 - Day 4 - Part 1
'''

FILE_PATH = "day_4/test.txt"
FILE_PATH = "day_4/input.txt"

def main():
    '''
    Implement solution to AoC - day 4 part 1
    '''

    with(open(FILE_PATH, 'r', encoding='utf-8')) as file:

        data = file.read()
        data = data.splitlines()
        data = [line.split(',') for line in data]
        data = [[x.split('-') for x in line] for line in data]
        data = [[(int(pair[0]), int(pair[1])) for pair in line] for line in data]

        # Each element in data is a pair of tuples
        # Each tuple is a range of numbers
        # Iterate over the pairs of tuples
        # We need to check if the range of one of the tuples is contained
        # by the other
        # If it is, then add one to counter
        counter = 0

        for pair in data:
            # Check if the first tuple is within range of the other
            if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
                counter += 1
            elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
                counter += 1

        print(counter)

if __name__ == "__main__":
    main()
