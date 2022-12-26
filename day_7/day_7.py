'''
Advent of Code Day 7

# Input
Each line in input is either a command or output from a unix terminal
Commands start with '$'
After an ls command, the output is a list of files and directories
Lines for directories start with 'dir' e.g. 'dir e'
Lines for files start with the file size and then the file name e.g. '2557 g'

# Output
For each directory, calculate the total size.
This includes any files in the directory, and the size of any subdirectories

# Data structures
Create a dictionary file_sizes with file names as keys and file sizes as values
Create a dictionary directories with directory names as keys and a list of
files and directories as values
Create a dictionary dir_size with directory names as keys and the total size as
values

'''

FILE_PATH = 'day_7/input.txt'
#FILE_PATH = 'day_7/test.txt'

def calc_dir_size(dir_name, directories, file_sizes):
    '''
    Calculate the size of a directory
    '''
    # Iterate over the list of files and directories
    # If the item is a file, add the file size to the total
    # If the item is a directory, call the function recursively
    # Return the total size
    total_size = 0

    for item in directories[dir_name]:
        if item.startswith('dir'):
            total_size += calc_dir_size(item.split(' ')[-1], directories,
                                        file_sizes)
        else:
            total_size += file_sizes[item]

    return total_size

def main():
    '''
    Implement AoC Day 7
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        data = data.splitlines()

        # Create a dictionary of directories as keys
        # Values are a list of files and directories
        # Keep track of full directory name
        # We need to do this because there may be multiple directories with the
        # same name
        # If we come across a file, add the file size to the file_sizes dict
        file_sizes = {}
        directories = {}
        current_dir = []
        current_dir_name = ''

        for line in data:
            # Special case when starting with root directory
            if line.startswith('$ cd /'):
                current_dir = ['root']
                current_dir_name = '/'.join(current_dir)
                directories[current_dir_name] = []
            elif line == '$ cd ..':
                current_dir.pop()
            # Add a new directory to directories dict
            elif line.startswith('$ cd'):
                current_dir.append(line.split(' ')[-1])
                current_dir_name = '/'.join(current_dir)
                directories[current_dir_name] = []
            elif line.startswith('$ ls'):
                continue
            elif line.startswith('dir'):
                directories[current_dir_name].append('dir ' + current_dir_name\
                    + '/' + line.split(' ')[-1])
            elif line[0].isdigit():
                file_size, file_name = line.split(' ')
                file_name = current_dir_name + '/' + file_name
                directories[current_dir_name].append(file_name)
                file_sizes[file_name] = int(file_size)

        # Now calculate the size of each directory
        dir_size = {}

        for dir_name in directories:
            dir_size[dir_name] = calc_dir_size(dir_name, directories,
                                               file_sizes)

        # Part 1
        # Get all directories with a size of at most 100000
        # Print the sum of these directory sizes
        result = 0
        for name, size in dir_size.items():
            if size <= 100000:
                result += size

        print(result)

        # Part 2
        # Total filesystem space is 70000000
        # Free space is 70000000 - size of root directory
        # Find the smallest directory such that if we delete it,
        # free space is at least 30000000

        free_space = 70000000 - dir_size['root']

        # Sort the directories by size
        # Iterate over the directories and find first directory
        # such that free_space + size >= 30000000
        sorted_dirs = sorted(dir_size.items(), key=lambda x: x[1])
        for name, size in sorted_dirs:
            if free_space + size >= 30000000:
                print(name, size)
                break

if __name__ == '__main__':
    main()
