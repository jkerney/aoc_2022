"""
Advent of Code 2022 - Day 13

- get indices of pairs that are in order

- iterate through list
- iterate through list and apply recursive function

- for loop to iterate through pairs
    - break for loop if in order and append to a list
    - return 1 if in order, -1 if not in order

- assume that the pairs of lists are never the same 

"""

FILE_PATH = "day_13/input.txt"
#FILE_PATH = "day_13/test.txt"

def test_order_fn(a, b):
    
    # Check if both integers
    #print(a,b)
    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
    elif type(a) == int and type(b) == list:
        a = [a]
    elif type(a) == list and type(b) == int:
        b = [b]

    # Now iterate through list a
    for i in range(len(a)):
        # First check if no item in list b
        if i >= len(b):
            return -1
        # Now compare the items by recursive call
        else:
            order_outcome = test_order_fn(a[i], b[i])
            if order_outcome == 0:
                continue
            else:
                return order_outcome

    if len(a) < len(b):
        return 1
    else:
        return 0

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.split('\n\n')
    text_data = [line.splitlines() for line in text_data]

    # Convert a string of nested list of integers into a nest list of integers
    data = [[eval(a) for a in line] for line in text_data]
    
    # Iterate over every pair
    order_result = []

    #pair = data[0]

    # just get it working for the first pair for now
    #a = pair[0]
    #b = pair[1]
    #print(test_order_fn(a,b))

    for pair in data:
        print("New pair: ", pair)
        a = pair[0]
        b = pair[1]
        print("Order: ", test_order_fn(a,b))
        order_result.append(test_order_fn(a,b))

    print(order_result)

    sum_indices = 0

    for i in range(len(order_result)):
        if order_result[i] == 1:
            sum_indices += i + 1

    print(sum_indices)
