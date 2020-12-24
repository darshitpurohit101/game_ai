import numpy as np
import random

class tic_tac_toe():
    
    def __init__(self):
        self.state = []
    
    def check_board(self, sboard):
        empty = []
        
        for row in range(len(board)):
            for box in range(len(board[row])):
                if board[row][box] == 0:
                    empty.append([row,box])
        if len(empty) == 0:
            return 0
        else:
            return empty
    
    def state_reg(self,board):
        current_state = []
        for x in board:
            for j in range(len(x)):
                current_state.append(x[j])
        return current_state
        
    def play(self, board):
        #Player one
        x,y = map(int,input("Human's turn! ").split(' '))
        board[(x,y)] = 1
        
        c_s = self.state_reg(board)
        self.state.append(c_s)
    
        possible_play = self.check_board(board)
        if possible_play == 0:
            print(self.state)
            return 0
        #player two
        selection = random.choice(possible_play)
        board[selection[0]][selection[1]] = 2
        
        c_s = self.state_reg(board)
        self.state.append(c_s)
        
        self.play(board)

board = np.array(np.zeros([3,3], dtype='int'))
c = tic_tac_toe()
c.play(board)

