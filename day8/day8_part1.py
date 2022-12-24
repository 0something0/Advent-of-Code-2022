
import numpy as np

#create variable with dummy array
forest_matrix = np.ndarray((0,0))

with open('day8_input.txt', 'r') as f:
    
    first_line = f.readline().strip()
    forest_matrix = np.asarray(list(first_line))

    for line in f:
        line = line.strip()
        forest_matrix = np.vstack((forest_matrix, np.asarray(list(line))))

print(forest_matrix)

# Minor setback 22:31 EDT - forgot to assign return value of np.vstack back to variable