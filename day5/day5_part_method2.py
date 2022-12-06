
from typing import List

#takes in each stack, returns each stack as a seperate list
def process_stacks(stacks: List[str]):

    #stacks should NOT have a newline at the end
    assert len(stacks[-1].strip()) != 0

    #remove the numeric labels (bottom line)
    stacks = stacks[:-1]

    #strip the leading and trailing bracket spaces
    new_stacks = []
    for line in stacks:
        line = line.strip('\n')
        line = line[1:-1]
        new_stacks.append(line)
    stacks = new_stacks

    #there's 4 characters between each container column, get only the containers and put them into a list
    stacks = [list(line[::4]) for line in stacks]

    print(stacks)
    stacks = list(zip(*stacks[::-1])) #https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    print(stacks)

    return stacks

def process_procedures(procedures: List[str]):
    
    procedures_list_dict = []
    for line in procedures:
        line = line.replace('move', '').replace('from', ' ').replace('to', ' ').split()
        procedures_list_dict.append({'quantity': line[0], 'source': line[1], 'target': line[1]})

    return procedures_list_dict

stacks_list = []
with open('stacks.txt') as stacks_file:
    stacks_list = process_stacks(stacks_file.readlines())

# Prepend blank list, such that the real lists start at 1
# I'm not dealing with bugs popping up from converting from 1-indexing (in the procedures) to 0-indexing
stacks_list = [[]] + stacks_list

print(stacks_list)