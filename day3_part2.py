from typing import TextIO

# reads next n lines from the given file
def read_multiple_lines(f: TextIO, num_lines):

    lines_list = []
    for i in range(num_lines):
        lines_list.append(f.readline().strip())

    return lines_list

priority_sum = 0
with open('day3_input') as f:

    #reads first 3 lines
    line_triplet = read_multiple_lines(f, 3)

    # continues until reaching end of file
    while all(line for line in line_triplet):
        
        #remove duplicate values
        line_triplet = [set(line) for line in line_triplet]

        print(line_triplet)

        # gets next set of line triple
        line_triplet = read_multiple_lines(f, 3)
