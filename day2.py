# Move      P1  P2  P2_winning_move
# Rock      A   X   Y
# Paper     B   Y   Z
# Scissor   C   Z   X

#winning moves probably can be calculated by ascii and modulo instead
winning_moves_dict = {'A': 'Y', 'B': "Z", 'C': 'X'}
move_scores_dict = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
with open("day2_input") as f:
    for line in f:
        move_list = line.split()
        
        #check if winning move by comparing winning move against P1 column with P2 column
        if winning_moves_dict[move_list[0]] == move_list[1]:
            print('win')
            score += (6 + move_scores_dict[move_list[1]])    
        
        #check for draw (both players do same move), (A, B, C) maps to (X, Y, Z) by ascii addition
        elif chr(ord(move_list[0]) + 23) == move_list[1]:
            print('draw')
            score += (3 + move_scores_dict[move_list[1]])
        
        #loss
        else:
            print('loss')
            score += move_scores_dict[move_list[1]]

print(score)