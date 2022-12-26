'''
Advent of Code - Day 5 Part 1

First part of input is multiple stacks of crates
Each row represents the crates in that y position for all stacks
Each crate is in the format [s] where s is a letter
There is a space separating each stack

The second part of the input is a sequence of instructions
Format is: 'move 1 from 2 to 1'
When moving a crate from one stack to the next,
the top crate is moved first

'''

#FILE_PATH = "day_5/test.txt"
FILE_PATH = "day_5/input.txt"

def main():
    '''
    Solve Day 5 Part 1
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        data = data.split('\n\n')

        # Get first part (stacks of crates) into a list of lists
        data_stacks = data[0].splitlines()
        # Get rid of last line which is just column numbers
        data_stacks.pop()
        num_stacks = int((len(data_stacks[0]) + 1)/4)
        stacks = [[] for _ in range(num_stacks)]

        # Go through each line and add crates to stack
        for line in data_stacks:
            for i in range(num_stacks):
                if line[i*4 + 1] != ' ':
                    stacks[i].append(line[i*4 + 1])

        # Get second part - instructions
        # Format is: move 1 from 2 to 1
        # Put into a list of lists
        data_instr = data[1].splitlines()
        data_instr = [line.split(' ') for line in data_instr]
        data_instr = [[int(line[1]), int(line[3]), int(line[5])] for line in data_instr]

        # Now execute instructions
        # First number in the list is the number of iterations
        # Second number is the stack to move from (pop)
        # Third number is the stack to insert into
        for instr in data_instr:
            for i in range(instr[0]):
                stacks[instr[2] - 1].insert(0, stacks[instr[1] - 1].pop(0))

        # Print the top crate of each stack
        top_stacks = ''
        for stack in stacks:
            top_stacks += stack[0]

        print(top_stacks)

if __name__ == "__main__":
    main()
