"""
Advent of Code 2022 - Day 14
https://adventofcode.com/2022/day/14

"""

#from ast import literal_eval
#import numpy

#FILE_PATH = "day_14/input.txt"
FILE_PATH = "day_14/test.txt"

def main():
    '''
    doc string here
    '''
    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()
        #text_data = text_data.split('\n\n')
        #text_data = [line.splitlines() for line in text_data]
        print(len(text_data))
        print(text_data[0])

if __name__ == "__main__":
    main()
