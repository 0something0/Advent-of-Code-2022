calorie_list = []

with open("day1_input", "r", newline="\n") as f:

    sum_calories = 0
    largest_value = 0

    for line in f:

        #check for actual content, then accumulate
        if line != '\n':
            sum_calories += int(line)

        # check for empty line delimiter
        # if is empty, push to list, compare with known largest value, reset accumulator
        elif line == '\n':
            calorie_list.append(sum_calories)
            largest_value = max(sum_calories, largest_value)
            sum_calories = 0
        
    # Manually push to list, since there's no empty line at end of file
    calorie_list.append(sum_calories)
    largest_value = max(sum_calories, largest_value)
    sum_calories = 0

print(largest_value)
calorie_list.sort()
print(sum(calorie_list[-3:]))

# its probably possible to keep this at O(n) by manually calculating the 3 largest values every time calorie_list is edited
# but I have way too much crap in my life already, I'm not dealing with this
