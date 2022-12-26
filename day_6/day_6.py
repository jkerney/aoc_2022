'''
Advent of Code - Day 6 - Part 1

Input is a string
Need to find the index of the first character
such that the previous four characters are unique
'''

FILE_PATH = 'day_6/input.txt'
#FILE_PATH = 'day_6/test.txt'

def main():
    '''
    Implement AoC - Day 6 Part 1
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read()

    # Iterate through the string
    # Start from position i = 0
    # Grab four characters starting from position i
    # Check if the four characters are unique
    # If unique, then break the for loop and print i + 4
    for i in range(0, len(data)-5):
        if len(set(data[i:i+4])) == 4:
            print(i+4)
            break

    # In part 2, we need to instead look for 14 unique characters
    for i in range(0, len(data)-14):
        if len(set(data[i:i+14])) == 14:
            print(i+14)
            break

if __name__ == "__main__":
    main()
