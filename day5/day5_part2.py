
from typing import List

#prints stacks in more readable format
def pretty_print_stacks(stack_lists):
    for stack in stacks_list[1:]:
        print(stack)

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

    #transpose matrix such that each row contains one stack
    #https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    stacks = list(zip(*stacks[::-1]))
    stacks = [list(val) for val in stacks]

    #trim the top of stacks
    for stack in stacks:
        while ' ' in stack:
            stack.remove(' ')

    return stacks

#turn the procedures text file into list of instruction dictionaries
def process_procedures(procedures: List[str]):
    
    #remove the words, convert chars into ints, and convert list into dict with named keys for readability
    procedures_list_dict = []
    for line in procedures:
        line = line.replace('move', '').replace('from', ' ').replace('to', ' ').split()
        line = [int(val) for val in line]
        procedures_list_dict.append({'quantity': line[0], 'source': line[1], 'target': line[2]})

    return procedures_list_dict

# Read file
stacks_list = []
with open('stacks.txt') as stacks_file:
    stacks_list = process_stacks(stacks_file.readlines())

# Prepend blank list, such that the real lists start at 1
# I'm not dealing with bugs popping up from converting from 1-indexing (in the procedures) to 0-indexing
stacks_list = [[]] + stacks_list

# Get list of procedures
procedures_list = []
with open('procedures.txt') as proc_f:
    procedures_list = process_procedures(proc_f)

# Execute each procedure
for count, procedures in enumerate(procedures_list):

    print(f'Procedure {count}\t' + str(procedures))
    print('Before')
    pretty_print_stacks(stacks_list)

    quantity = procedures['quantity']
    source = procedures['source']
    target = procedures['target']

    #remove the given quantity of containers from source stack
    val = stacks_list[source][-1 * quantity:]
    stacks_list[source] = stacks_list[source][:-1 * quantity]

    print(f'During, {val} in transit')
    pretty_print_stacks(stacks_list)

    #stack the containers onto destination
    stacks_list[target] += val
    
    print('After')
    pretty_print_stacks(stacks_list)
    print('')

# Get answer string ()
top_list = ""
for stack in stacks_list[1:]:
    top_list += stack[-1]

print(top_list)

