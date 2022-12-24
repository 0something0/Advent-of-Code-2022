folder_size_target = 358913 #calculated manually

def close_directory(stack: list, list_of_dirs_over_target: list):
    
    # Check if current directory has size greater than target
    if stack[-1][1] >= folder_size_target:
        list_of_dirs_over_target.append(stack[-1])
    
    # Add current directory size to parent dir size
    stack[-2][1] += stack[-1][1]
    stack.pop()

    return stack, list_of_dirs_over_target

with open('day7_input.txt', 'r') as f:

    stack = [ ['/', 0] ]
    list_of_dirs_over_target = []

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
            stack, list_of_dirs_over_target = close_directory(stack, list_of_dirs_over_target)

        # Entering directory
        elif line.strip()[:5] == '$ cd ':
            stack.append([ line.strip().split()[-1], 0])
    
        # Check if line contains a directory size
        # Split line into two, attempt casat zeroth element to integer
        # Relies on *every* other filter working, else casting will fail due to non-directory size text
        elif int(line.split()[0]):
            file_size = int(line.split()[0])
            stack[-1][1] = file_size + stack[-1][1]
        
        # print(line.strip())
        # print(stack)
        # print(stack_dirname)
        print(list_of_dirs_over_target)

    # clean up stack at the end
    # Check if current directory has size greater than target
    # NOTE - can't close root directory, is this a bug?
    while len(stack) > 1:
        stack, list_of_dirs_over_target = close_directory(stack, list_of_dirs_over_target)
        print(stack)
        print(list_of_dirs_over_target)

    # Sort by size then search for smallest candidate directory
    from operator import itemgetter, attrgetter

    sorted_list = sorted(list_of_dirs_over_target, key=itemgetter(1))
    print(sorted_list)

    # Actually we are NOT going to do that

    # Get pure list of sizes, and run the min function with a custom function for search value/key
    names_list, dir_list = list(zip(*list_of_dirs_over_target))
    print(dir_list)
    min_val = min(dir_list, key=lambda x:((x-folder_size_target, folder_size_target)[int(x-folder_size_target < 0)]))
    print(min_val)

# Setback 1: Failed to read instructions properly, leading to me inputting incorrect target bounds