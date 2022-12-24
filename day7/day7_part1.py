

with open('day7_input.txt', 'r') as f:


    stack = [0]

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

        # Entering directory
        elif line.strip()[:-1] == '$ cd ':
            # stack.append(0)
            # print(stack)
            pass

        # Exiting directory
        elif line.strip() == '$ cd ..':
            pass
    
        # Check if line contains a directory size
        # Split line into two, attempt casat zeroth element to integer
        # Relies on *every* other filter working, else casting will fail due to non-directory size text
        elif int(line.split()[0]):
            file_size = int(line.split()[0])
            stack[-1] = file_size + stack[-1]

        print(stack)
