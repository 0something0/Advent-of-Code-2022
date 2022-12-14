
from typing import List
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

    return stacks

def process_procedures(procedures: List[str]):
    
    procedures_list_dict = []
    for line in procedures:
        line = line.replace('move', '').replace('from', ' ').replace('to', ' ').split()
        procedures_list_dict.append({'quantity': line[0], 'source': line[1], 'target': line[1]})

    return procedures_list_dict

stacks_ndlist = []
with open('stacks.txt') as stacks_file:
    stacks_ndlist = process_stacks(stacks_file.readlines())

#convert to numpy ndarray because I can't be bothered to do multidimensional work manually
import numpy as np
stacks = np.array(stacks_ndlist)

# Prepend blank column, such that array columns start at 1
# I'm not dealing with bugs popping up from converting from 1-indexing (in the procedures) to 0-indexing
stacks = np.hstack([np.full((len(stacks), 1), ' '), stacks])

print(stacks)

# Read procedures from list of files as dict
procedures_list = []
with open('procedures.txt') as proc_f:
    procedures_list = process_procedures(proc_f)
