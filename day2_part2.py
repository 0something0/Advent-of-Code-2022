# Move      P1 
# Rock      A  
# Paper     B  
# Scissor   C  

# Instruction Decode
# X           Lose
# Y           Draw
# Z           Win

#winning moves probably can be calculated by ascii and modulo instead
winning_moves_dict ={'A': 'P', 'B': 'S', 'C': 'R'}
tie_moves_dict =    {'A': 'R', 'B': 'P', 'C': 'S'}
lose_moves_dict =   {'A': 'S', 'B': 'R', 'C': 'P'}

move_scores_dict = {'R': 1, 'P': 2, 'S': 3}

def calculate_score_change(opponent_move, instruction):

    if instruction == 'X':
        return 0 + move_scores_dict[lose_moves_dict[opponent_move]]

    if instruction == 'Y':
        return 3 + move_scores_dict[tie_moves_dict[opponent_move]]

    if instruction == 'Z':
        return 6 + move_scores_dict[winning_moves_dict[opponent_move]]
    else:
        raise ValueError('instruction should be X, Y, or Z')

score = 0
with open("day2_input") as f:
    for line in f:
        move_list = line.split()
        score += calculate_score_change(move_list[0], move_list[1])

print(score)