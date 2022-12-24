

# checks if string has duplicate (non-unque) characters 
# gets each character, and checks if it occurs more than once

def has_dupliciate_char(string: str) -> bool:

    for char in string:
        if string.count(char) > 1:
            return True

    return False

with open('day6_input.txt', 'r') as f:

    # input should be a single (very long) line
    line = f.readline()

    # increments cursor and checks last 4 characters before cursor (scan_string)
    for i in range(4, len(line)):

        scan_string = line[i-4: i]
        has_dupliciate = has_dupliciate_char(scan_string)
        
        if not has_dupliciate:
            print(f'{scan_string}\n{i}')
            break