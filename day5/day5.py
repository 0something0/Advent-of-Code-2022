

def process_stacks(stacks: str):

    #stacks should NOT have a newline at the end
    assert len(stacks[-1].strip()) != 0

    #remove the numeric labels (bottom line)
    stacks = stacks[:-1]
    print(stacks)

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


stacks_ndlist = []
with open('stacks.txt') as stacks_file:
    stacks_ndlist = process_stacks(stacks_file.readlines())

print(stacks_ndlist)