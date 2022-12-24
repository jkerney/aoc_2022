"""
Advent of Code 2022 - Day 15 Part 1
https://adventofcode.com/2022/day/15
"""

#from ast import literal_eval
#import numpy
#import itertools
import re

FILE_PATH = "day_15/input.txt"
#FILE_PATH = "day_15/test.txt"

def main():
    '''
    Day 15 Part 1
    '''

    # Check how many positions on this row we know don't have a beacon
    y_test = 2000000

    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()
        text_data = [re.findall(r"x=(-?\d+), y=(-?\d+)", line) for line in text_data]
        text_data = [[(int(a), int(b)) for (a,b) in line] for line in text_data]

        no_beacon = []
        dist_beacon = []

        for sensor, beacon in text_data:
            
            # Distance from sensor to closest beacon
            dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

            # Now check distance to line y_test
            dist_y_test = abs(sensor[1] - y_test)

            # Check if any point on y_test line is closer than the beacon
            if dist_y_test <= dist:

                no_beacon.append((sensor[0], y_test))

                for i in range(1, dist - dist_y_test + 1):
                    no_beacon.append((sensor[0] - i, y_test))
                    no_beacon.append((sensor[0] + i, y_test))

        no_beacon = set(no_beacon)
        # Remove beacons from the set
        for sensor, beacon in text_data:
            try:
                no_beacon.remove(beacon)
            except:
                pass

        print(len(set(no_beacon)))

if __name__ == "__main__":
    main()
