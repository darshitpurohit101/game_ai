import numpy as np
import random

def check_board(board):
    empty = []
    
    for row in range(len(board)):
        for box in range(len(board[row])):
            if board[row][box] == 0:
                empty.append([row,box])
    if len(empty) == 0:
        return 0
    else:
        return empty

def state_reg(board):
    current_state = []
    for x in board:
        for j in range(len(x)):
            current_state.append(x[j])
    return current_state
    
def play(board):
    state = []
    #Player one
    x,y = map(int,input("Human's turn! ").split(' '))
    board[(x,y)] = 1
    
    c_s = state_reg(board)
    state.append(c_s)

    possible_play = check_board(board)
    if possible_play == 0:
        print(state)
        return 0
    #player two
    selection = random.choice(possible_play)
    board[selection[0]][selection[1]] = 2
    
    c_s = state_reg(board)
    state.append(c_s)
    
    play(board)

board = np.array(np.zeros([3,3], dtype='int'))
play(board)

