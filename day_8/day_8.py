'''
AoC - Day 8

## Part 1

# Input
Input is a grid of trees. Each char is a number 0-9 that represents the height
of the tree.
Each line is a row of the grid

# Calculate
Check if a tree is visible from outside the grid
Check in four directions: up, down, left, right
A tree is visible if it is taller than all other trees between itself and the
edge of the grid

# Data Structures
Represent the grid as a list of lists
Each list is a column of the grid

# Output
How many trees are visible from outside the grid
'''

FILE_PATH = "day_8/input.txt"
#FILE_PATH = "day_8/test.txt"

def is_visible(grid, x_pos, y_pos):
    '''
    Check if a tree is visible from outside the grid
    '''
    # Check up
    tree_visible = True
    for index in range(y_pos - 1, -1, -1):
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            tree_visible = False

    if tree_visible:
        return True

    # Check down
    tree_visible = True
    for index in range(y_pos + 1, len(grid[x_pos])):
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            tree_visible = False

    if tree_visible:
        return True

    # Check left
    tree_visible = True
    for index in range(x_pos - 1, -1, -1):
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            tree_visible = False

    if tree_visible:
        return True

    # Check right
    tree_visible = True
    for index in range(x_pos + 1, len(grid)):
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            tree_visible = False

    if tree_visible:
        return True
    else:
        return False

def main():
    '''
    Implement Day 8 Part 1
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        data = data.splitlines()

        # Create the data structure for the grid
        grid = [[] for _ in range(len(data[0]))]
        for line in data:
            for index, char in enumerate(line):
                grid[index].append(int(char))

        # Check if a tree is visible from outside the grid
        # Don't bother checking trees on the edge of the grid
        # For each tree, check up, down, left, right
        visible_trees = len(grid) * 2 + len(grid[0]) * 2 - 4
        for x_pos in range(1, len(grid) - 1):
            for y_pos in range(1, len(grid[x_pos]) - 1):
                if is_visible(grid, x_pos, y_pos):
                    visible_trees += 1

        print(visible_trees)

if __name__ == "__main__":
    main()