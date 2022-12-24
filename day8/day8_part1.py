
import numpy as np

#create variable with dummy array
forest_matrix = np.ndarray((0,0))

with open('day8_input.txt', 'r') as f:
    
    #initializes array width using first line
    first_line = f.readline().strip()
    forest_matrix = np.asarray(list(first_line))

    #stacks the remaining lines onto first line with a lot of casting 
    for line in f:
        line = line.strip()
        line = list(line)
        line = [int(num) for num in line]
        forest_matrix = np.vstack((forest_matrix, np.asarray(line)))

print(forest_matrix)


is_hidden_matrix = np.ndarray(forest_matrix.shape, dtype=bool)
is_hidden_matrix.fill(False)

for (row, col), value in np.ndenumerate(forest_matrix):

    # This is somewhat less efficient then solutions that do not involve enumerating the edge cells
    # ,but this solution is easier for my tiny brai-err I mean "more maintainable"

    # Check if NOT edge cells
    if row > 0 and col > 0 and row < len(forest_matrix) - 1 and col < len(forest_matrix[0]) - 1:

        curr_val = forest_matrix[row][col]
        print(curr_val)

        #check if up, down, left, right are greater than or equal to current tree
        is_hidden = forest_matrix[row - 1][col] >= curr_val and \
                    forest_matrix[row + 1][col] >= curr_val and \
                    forest_matrix[row][col - 1] >= curr_val and \
                    forest_matrix[row][col + 1] >= curr_val

        is_hidden_matrix[row][col] = is_hidden

print(is_hidden_matrix)

# Minor setback 22:31 EDT - forgot to assign return value of np.vstack back to variable
# Minor setback 22:43 EDT - np.ndenumerate enumerates from zero when slicing