"""
Advent of Code 2022 - Day 15 Part 2
https://adventofcode.com/2022/day/15

This is very slow. Non-optimum solution for now.
Maybe takes an hour? Committing for now until
I can find a better solution.

"""

#from ast import literal_eval
#import numpy
#import itertools
import re

FILE_PATH = "day_15/input.txt"
#FILE_PATH = "day_15/test.txt"
MAX_COORD = 4000000
COUNTER_ITR = 100000

def add_point(points_check, x, y):
    '''
    Check if point is within bounds and add to set
    '''
    if x < MAX_COORD and y < MAX_COORD and x >= 0 and y >= 0:
        points_check.add((x,y))

def main():
    '''
    Day 15 Part 2
    '''

    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()
        text_data = [re.findall(r"x=(-?\d+), y=(-?\d+)", line) for line in text_data]
        data = [[(int(a), int(b)) for (a,b) in line] for line in text_data]
        data_with_dist = []

        points_check = set()

        print("Adding points to check for each sensor")
        for sensor, beacon in data:
            # Distance from sensor to closest beacon
            dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            data_with_dist.append((sensor, beacon, dist))
            print("Sensor location", sensor)

            # Now iterate over every point that is dist+1 away
            for i in range(dist+1):

                x = sensor[0] + i
                y = sensor[1] + (dist + 1 - i)
                add_point(points_check, x, y)

                x = sensor[0] + i
                y = sensor[1] - (dist + 1 - i)
                add_point(points_check, x, y)

                if i > 0:
                    x = sensor[0] - i
                    y = sensor[1] + (dist + 1 - i)
                    add_point(points_check, x, y)

                    x = sensor[0] - i
                    y = sensor[1] - (dist + 1 - i)
                    add_point(points_check, x, y)

        print("Completed adding points to check")
        print("Number points to check:", len(points_check))
        
        counter = 0
        # now for these points, check if they're within distance of any other sensor
        for point in points_check:
            counter += 1
            if counter % COUNTER_ITR == 0:
                print("Completed", counter, "points")
            emergency_beacon = True
            for sensor, beacon, dist in data_with_dist:
                if abs(sensor[0] - point[0]) + abs(sensor[1] - point[1]) <= dist:
                    emergency_beacon = False
                    break

            if emergency_beacon == True:
                print("Location of emergency beacon:", point)
                print("Tuning frequency", point[0] * 4000000 + point[1])
                break

if __name__ == "__main__":
    main()
