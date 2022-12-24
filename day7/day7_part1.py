def close_directory(stack: list, list_of_dirs_under_100k: list):
    
    # Check if current directory has size less than 100k
    if stack[-1][1] <= 100000:
        list_of_dirs_under_100k.append(stack[-1])
    
    # Add current directory size to parent dir size
    stack[-2][1] += stack[-1][1]
    stack.pop()

    return stack, list_of_dirs_under_100k

with open('day7_input.txt', 'r') as f:

    stack = [ ['/', 0] ]
    list_of_dirs_under_100k = []

    for line in f:

        # Cases:
        # cd /
        # cd <directory>
        # cd ..
        # ls
        # <file size> [fileename]
        # dir [directory name]

        # Filter for filler output
        if line.strip() == '$ cd /' or line.strip() == '$ ls' or line.strip()[:3] == 'dir':
            pass

        # Exiting directory
        elif line.strip() == '$ cd ..':
            stack, list_of_dirs_under_100k = close_directory(stack, list_of_dirs_under_100k)

        # Entering directory
        elif line.strip()[:5] == '$ cd ':
            stack.append([ line.strip().split()[-1], 0])
    
        # Check if line contains a directory size
        # Split line into two, attempt casat zeroth element to integer
        # Relies on *every* other filter working, else casting will fail due to non-directory size text
        elif int(line.split()[0]):
            file_size = int(line.split()[0])
            stack[-1][1] = file_size + stack[-1][1]
        
        #print(line.strip())
        # print(stack)
        # print(stack_dirname)
        # print(list_of_dirs_under_100k)

    # clean up stack at the end
    # Check if current directory has size less than 100k
    # NOTE - can't close root directory, is this a bug?
    while len(stack) > 1:
        stack, list_of_dirs_under_100k = close_directory(stack, list_of_dirs_under_100k)
        print(stack)
        print(list_of_dirs_under_100k)

    # Sum directories under 100k to get final answer
    sum_dir_sizes = 0
    for dir in list_of_dirs_under_100k:
        sum_dir_sizes += dir[1]
    
    print(sum_dir_sizes)

# Setback 1 - given test data only had 1-char directory names, so program only checked for 1-char directories
#             whereas real data has longer dir names
# Setback 1.1 - filtering for 'cd ..' is more strict and so should have taken precdence
#               ,but 'cd [dirname]' came first, causing '..' to be included in filenames 