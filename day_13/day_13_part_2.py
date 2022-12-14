"""
Advent of Code 2022 - Day 13 - Part 2
https://adventofcode.com/2022/day/13
"""

from ast import literal_eval
import functools

FILE_PATH = "day_13/input.txt"
#FILE_PATH = "day_13/test.txt"

def test_order_fn(item_a, item_b):
    '''
    Recursive function - check if lists are ordered
    according to problem definition
    '''
    # Directly calculate order if both integers
    #print(a,b)
    if isinstance(item_a, int) and isinstance(item_b, int):
        if item_a < item_b:
            return -1
        elif item_a > item_b:
            return 1
        else:
            return 0
    elif isinstance(item_a, int) and isinstance(item_b, list):
        item_a = [item_a]
    elif isinstance(item_a, list) and isinstance(item_b, int):
        item_b = [item_b]

    # Now iterate through list a
    for i in range(len(item_a)):
        # First check if no item in list b
        if i >= len(item_b):
            return 1
        # Now compare the items by recursive call
        else:
            order_outcome = test_order_fn(item_a[i], item_b[i])
            if order_outcome == 0:
                continue
            else:
                return order_outcome
 
    # Check if run out of items in a
    if len(item_a) < len(item_b):
        return -1
    else:
        return 0

def main():
    '''
    Part 2: order all lines in input file
    Add [[2]] and [[2]] to the end of the list
    Sort the list
    Find the indices of [[2]] and [[6]]
    Multiply the indices
    '''
    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.splitlines()
        #remove empty strings from list
        text_data = [line for line in text_data if line]

        # Convert string of nested lists into python lists
        data = [literal_eval(a) for a in text_data]
        # Add divider packets
        data.append([[2]])
        data.append([[6]])
        sorted_data = sorted(data, key=functools.cmp_to_key(test_order_fn))

        # Get indices of [[2]] and [[6]]
        index_2 = sorted_data.index([[2]]) + 1
        index_6 = sorted_data.index([[6]]) + 1
        print(index_2 * index_6)

if __name__ == "__main__":
    main()
