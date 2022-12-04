
with open("day4_input") as f:
    
    counter_containing = 0
    for line in f:
        
        #process input into 2D list of numbers
        assignments = line.strip().split(',')
        assignments = [assign_range.split('-') for assign_range in assignments]

        print(assignments)

        #compare ranges

        # zeroth range fully contains first range
        if assignments[0][0] <= assignments[1][0] and assignments[0][1] >= assignments[1][1]:
            counter_containing += 1
            print("enclosing")

        # first range fully contains zeroth range
        elif assignments[0][0] >= assignments[1][0] and assignments[0][1] <= assignments[1][1]:
            counter_containing += 1
            print("enclosing")

    print(counter_containing)