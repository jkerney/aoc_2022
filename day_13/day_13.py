"""
Advent of Code 2022 - Day 13

- get indices of pairs that are in order

- iterate through list
- iterate through list and apply recursive function

- for loop to iterate through pairs
    - break for loop if in order and append to a list
    - return 1 if in order, -1 if not in order

- function
- 
- 

"""

#FILE_PATH = "day_13/input.txt"
FILE_PATH = "day_13/test.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.split('\n\n')
    text_data = [line.splitlines() for line in text_data]

    # Convert a string of nested list of integers into a nest list of integers
    data = [[eval(a) for a in line] for line in text_data]
    
    # Iterate over every pair

    order_result = []

    for pair in data:
        a = pair[0]
        b = pair[1]
        #print(a,b)
        order_result.append(test_order_fn(a,b))

def test_order_fn(a, b):
    # Check if both integers
    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        elif a > b:
            return -1
        else
            return 0
    elif type(a) == int and type(b) == list:
        a = list(a)
    elif type(a) == list and type(b) == int:
        b = list(b)
    
    return order_result(a, b)