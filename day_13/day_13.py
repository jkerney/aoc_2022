"""
Advent of Code 2022 - Day 13
https://adventofcode.com/2022/day/13

"""

from ast import literal_eval

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
            return 1
        elif item_a > item_b:
            return -1
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
            return -1
        # Now compare the items by recursive call
        else:
            order_outcome = test_order_fn(item_a[i], item_b[i])
            if order_outcome == 0:
                continue
            else:
                return order_outcome
 
    # Check if run out of items in a
    if len(item_a) < len(item_b):
        return 1
    else:
        return 0

def main():
    '''
    Part 1: Find the sum of the indices of all ordered pairs
    '''
    with open(FILE_PATH, "r", encoding="utf-8") as input_file:

        text_data = input_file.read()
        text_data = text_data.split('\n\n')
        text_data = [line.splitlines() for line in text_data]

        # Convert string of nested lists into python lists
        data = [[literal_eval(a) for a in line] for line in text_data]

        # Iterate over every pair and get order outcome
        order_result = []

        for pair in data:
            print("New pair: ", pair)
            outcome = test_order_fn(pair[0],pair[1])
            order_result.append(outcome)
            print("Order: ", outcome)

        print(order_result)

        # Get the sum of the indices of all ordered pairs
        sum_indices = 0

        for i, outcome in enumerate(order_result):
            if outcome == 1:
                sum_indices += i + 1

        print(sum_indices)


if __name__ == "__main__":
    main()
