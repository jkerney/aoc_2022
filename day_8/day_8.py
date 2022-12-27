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

## Part 1

# Calculate
For each tree, calculate the scenic score
Scenic score is calculated by checking up, down, left, right
Find how many trees until we find one that is the same height or taller,
or we reach the edge
Scenic score is then number of trees found in each direction multiplied

# Output
Highest scenic score in the grid

'''

FILE_PATH = "day_8/input.txt"
#FILE_PATH = "day_8/test.txt"

def is_visible(grid, x_pos, y_pos):
    '''
    Check if a tree is visible from outside the grid
    '''
    visible_up = True
    visible_down = True
    visible_left = True
    visible_right = True

    # Check up
    for index in range(y_pos - 1, -1, -1):
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            visible_up = False

    # Check down
    for index in range(y_pos + 1, len(grid[x_pos])):
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            visible_down = False

    # Check left
    for index in range(x_pos - 1, -1, -1):
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            visible_left = False

    # Check right
    for index in range(x_pos + 1, len(grid)):
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            visible_right = False

    return max(visible_up, visible_down, visible_left, visible_right)

def scenic_score(grid, x_pos, y_pos):
    '''
    Calculate the scenic score for the tree
    '''
    scenic_up = 0
    scenic_down = 0
    scenic_left = 0
    scenic_right = 0

    # Check up
    for index in range(y_pos - 1, -1, -1):
        scenic_up += 1
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            break

    # Check down
    for index in range(y_pos + 1, len(grid[x_pos])):
        scenic_down += 1
        if grid[x_pos][index] >= grid[x_pos][y_pos]:
            break

    # Check left
    for index in range(x_pos - 1, -1, -1):
        scenic_left += 1
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            break

    # Check right
    for index in range(x_pos + 1, len(grid)):
        scenic_right += 1
        if grid[index][y_pos] >= grid[x_pos][y_pos]:
            break

    return scenic_up * scenic_down * scenic_left * scenic_right

def main():
    '''
    Implement Day 8 Part 1
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        data = data.splitlines()

        # Create the data structure for the grid
        # Each list within the list is a column
        # This means we can address the grid using grid[x][y]
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

        print("Part 1:", visible_trees)

        # Part 2
        # Calculate scenic score for all trees not on the edge
        # Trees on the edge will always have a score of 0
        scenic_scores = []
        for x_pos in range(1, len(grid) - 1):
            for y_pos in range(1, len(grid[x_pos]) - 1):
                scenic_scores.append(scenic_score(grid, x_pos, y_pos))

        print("Part 2:", max(scenic_scores))

if __name__ == "__main__":
    main()
