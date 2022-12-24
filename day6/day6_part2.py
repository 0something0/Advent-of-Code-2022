

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

    # increments cursor and checks last n characters before cursor (scan_string)

    scan_buffer_size = 14

    for i in range(scan_buffer_size, len(line)):

        scan_string = line[i-scan_buffer_size: i]
        has_dupliciate = has_dupliciate_char(scan_string)
        
        if not has_dupliciate:
            print(f'{scan_string}\n{i}')
            break

# Day 6 was easy, no significant setbacks on neither parts, though there was an off by one error while getting the range() in part 1