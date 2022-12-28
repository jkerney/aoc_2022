'''
Advent of Code - Day 9 - Part 1

# Input
A sequence of moves. Example format 'R 4'.
The first character is one of the four directions: U, D, L, R.
The second character is how many positions the head moves

# Calculation
For each move, need to calculate the position of the head and the tail.
The head moves in the direction specified by the move.
The tail moves in the following direction

Head and tail are touching if the head is directly up, down, left, right, or
diagonal to the tail.

If the head and tail aren't touching:
    -  If head is in same row or column, then the tail moves one position
    towards the head
    - If head is in a different row and column, then the tail moves one
    position diagonally towards the head

# Output - Part 1
How many positions does the tail visit at least once?

'''

FILE_PATH = "day_9/input.txt"
#FILE_PATH = "day_9/test.txt"

def update_tail(head_pos, tail_pos):
    '''
    Update the position of the tail based on the position of the head
    '''

    # Cases to consider
    # Head and tail are touching - no change to tail_pos
    if (head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]) or\
    (head_pos[0] == tail_pos[0] and abs(head_pos[1] - tail_pos[1]) == 1) or\
    (head_pos[1] == tail_pos[1] and abs(head_pos[0] - tail_pos[0]) == 1) or\
    (abs(head_pos[0] - tail_pos[0]) == 1 and abs(head_pos[1] - tail_pos[1]\
    ) == 1):
        return tail_pos

    # Head and tail are in same row or column, but not touching
    if head_pos[0] == tail_pos[0]:
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1
    # Head and tail are in same column, but not touching
    elif head_pos[1] == tail_pos[1]:
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
    # Head and tail are in different row and column - up and right
    elif head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
        tail_pos[0] += 1
        tail_pos[1] += 1
    # Head and tail are in different row and column - up and left
    elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
        tail_pos[0] -= 1
        tail_pos[1] += 1
    # Head and tail are in different row and column - down and right
    elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
        tail_pos[0] += 1
        tail_pos[1] -= 1
    # Head and tail are in different row and column - down and left
    elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
        tail_pos[0] -= 1
        tail_pos[1] -= 1

    return tail_pos

def main():
    '''
    Implement Day 9 Part 1
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:

        moves = input_file.read().splitlines()
        moves = [move.split(' ') for move in moves]
        moves = [(move[0], int(move[1])) for move in moves]

        # Iterate through moves and calculate position of the head and tail
        # Head and tail start at (0,0)
        head_pos = [0,0]
        tail_pos = [0,0]
        tail_pos_record = []
        for direction, itr in moves:
            for _ in range(itr):
                if direction == 'U':
                    head_pos[1] += 1
                elif direction == 'D':
                    head_pos[1] -= 1
                elif direction == 'L':
                    head_pos[0] -= 1
                elif direction == 'R':
                    head_pos[0] += 1

                tail_pos = update_tail(head_pos, tail_pos)
                tail_pos_record.append((tail_pos[0], tail_pos[1]))

        # Count how many positions the tail visits at least once
        tail_pos_record = [(x,y) for x,y in tail_pos_record]
        print(len(set(tail_pos_record)))

if __name__ == "__main__":
    main()
