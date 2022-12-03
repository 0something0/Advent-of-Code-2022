
# returns priority number for each item type
# a-z (lowercase) are given 1-26 respectively, 
# A-Z (uppercase) are given 27-52

def get_priority(char: str):
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char) - 65 + 27

priority_sum = 0
with open('day3_input') as f:

    for line in f:
        
        # gets list of unique items in compartment by splitting line into half
        half_length = int(len(line.strip()) / 2)
        compartment_1 = set(line[:half_length])
        compartment_2 = set(line[half_length:])

        # searches for duplicate items across both compartment by
        # getting each item from compartment_1, and comparing it with every other item
        # in compartment_2

        for char1 in compartment_1:
            for char2 in compartment_2:
                if char1 == char2:
                    print(get_priority(char1))
                    priority_sum += get_priority(char1)

print(priority_sum)

# 1 wrong submission - caused by 
#        return ord(char) - 65 + 27
# instead of 
#         return ord(char) - 64 + 27
# which was from earler test that assumed that uppercase priorities also started from 1 instead of 28, that was "fixed"