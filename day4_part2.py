# sort numbers a-b,x-y in ascending order

# case 1 
# a < x < b < y

# case 2
# x < a < y < b

# case 3
# x < a < b < y

# case 4
# a < x < y < b


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
        #e.g. first range crosses zeroth range upper boundary
        if a <= x and x <= b and b <= y:
            counter_containing += 1
            print('containing (zeroth < first)')

        #zeroth range ends above first range
        #e.g. zeroth range crosses first range upper boundary
        elif x <= a and a <= y and y <= b:
            counter_containing += 1
            print('containing (first < zeroth)')

        #completely containing (no overlap)
        # zeroth range fully contains first range
        elif a < x and y < b:
            counter_containing += 1
            print("zeroth contains first")

        # first range fully contains zeroth range
        elif x < a and b < y:
            counter_containing += 1
            print("first contains zeroth")

    print(counter_containing)

#first attempt - incorrect because I forgot to account for completely overlapping cases