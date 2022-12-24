

with open('day7_input.txt', 'r') as f:


    for line in f:

        # cases:
        # cd /
        # cd <directory>
        # cd ..
        # ls
        # <file size> [fileename]
        # dir [directory name]

        if line.strip() == '$ cd /' or line.strip() == '$ ls' or line.strip()[:2] == 'dir':
            pass
        else:
            print(line)