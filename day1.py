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