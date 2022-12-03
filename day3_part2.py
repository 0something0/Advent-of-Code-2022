from typing import TextIO

def get_priority(char: str):
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char) - 65 + 27

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

        for char1 in line_triplet[0]:
            for char2 in line_triplet[1]:
                for char3 in line_triplet[2]:
                    if char1 == char2 and char2 == char3:
                        priority_sum += get_priority(char1)

        # gets next set of line triple
        line_triplet = read_multiple_lines(f, 3)

print(priority_sum)