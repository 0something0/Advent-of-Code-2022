# sort numbers a-b,x-y in ascending order

# case 1 
# a < x < b < y

# case 2
# x < a < y < b

# check if x is less than b and b is greater than y

with open("day4_input") as f:
    
    counter_containing = 0
    for line in f:
        
        #process input into 2D list of numbers
        assignments = line.strip().split(',')
        assignments = [ [int(string) for string in assign_range.split('-')] for assign_range in assignments]

        print(assignments)

        #compare ranges

        a = assignments[0][0]
        b = assignments[0][1]
        x = assignments[1][0]
        y = assignments[1][1]

        #first range ends above zeroth range
        if a <= x and x <= b and b <= y:
            counter_containing += 1
            print('containing')
        elif x <= a and a <= y and y <= b:
            counter_containing += 1
            print('containing')

    print(counter_containing)

