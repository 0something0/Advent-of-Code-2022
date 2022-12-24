def close_directory():
    pass

with open('day7_input.txt', 'r') as f:

    stack = [0]
    stack_dirname = ['/']
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

            if stack[-1] <= 100000:
                list_of_dirs_under_100k.append(stack_dirname[-1])

            stack[-2] += stack[-1]
            stack.pop()
            stack_dirname.pop()

        # Entering directory
        elif line.strip()[:5] == '$ cd ':
            stack.append(0)
            print(line)
            stack_dirname.append(line.strip().split()[-1])
    
        # Check if line contains a directory size
        # Split line into two, attempt casat zeroth element to integer
        # Relies on *every* other filter working, else casting will fail due to non-directory size text
        elif int(line.split()[0]):
            file_size = int(line.split()[0])
            stack[-1] = file_size + stack[-1]

        print(stack)
        print(stack_dirname)
        print(list_of_dirs_under_100k)

    # clean up stack at the end
    if stack[-1] <= 100000:
        list_of_dirs_under_100k.append(stack_dirname[-1])

    stack[-2] += stack[-1]
    stack.pop()
    stack_dirname.pop()

    print(stack)
    print(stack_dirname)
    print(list_of_dirs_under_100k)

# Setback 1 - given test data only had 1-char directory names, so program only checked for 1-char directories
#             whereas real data has longer dir names
# Setback 1.1 - filtering for 'cd ..' is more strict and so should have taken precdence
#               ,but 'cd [dirname]' came first, causing '..' to be included in filenames 