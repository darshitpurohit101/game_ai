import numpy as np
import random

class tic_tac_toe():
    
    def __init__(self):
        self.state = []
    
    def row(self, board, player):
        
        for i in range(3):
            w = True
            for j in range(3):
                if board[i][j] != player:
                    w = False
            
            return w
            
    def col(self, board, player):
        
        for i in range(3):
            w = True
            for j in range(3):
                if board[j][i] != player:
                    w = False
            
            return w
                
    def diag(self, board, player):
        
        win = True
        
        for i in range(3): 
            if board[i, i] != player: 
                win = False
                
        return(win) 
        
    def reward(self, winner, p):
        
        if winner == 0:
            return 0
        elif winner == p:
            return 1
        elif winner == -1:
            return 1
        else:
            return -1
            
    def elvaluate(self, board, p):
        
        winner = 0
        p = p
        
        for player in [1, 2]: 
            if (self.row(board, player) or
                self.col(board, player) or
                self.diag(board, player)): 
                winner = player
            
            if np.all(board != 0) and winner == 0: 
                winner = -1
    	
        result = self.reward(winner, p)
        return result, winner
        
    
    def check_board(self, sboard):
        empty = []
        
        for row in range(len(board)):
            for box in range(len(board[row])):
                if board[row][box] == 0:
                    empty.append([row,box])
    
        return empty
    
    def state_reg(self,board):
        current_state = []
        for x in board:
            for j in range(len(x)):
                current_state.append(x[j])
        return current_state
        
    def play(self, board, game):
        #Player one
        game = game
        print(board)
        x,y = map(int,input("Human's turn! ").split(' '))
        if board[(x,y)] !=0 :
            x,y = map(int,input("Choose diff box! ").split(' '))
            board[(x,y)] = 1
        else:
            board[(x,y)] = 1
        
        c_s = self.state_reg(board)
        self.state.append(c_s)
        
        state_reward, point = self.elvaluate(board, 1)
        if point != 0:
            print("player 1: "+str(state_reward))
            print(self.state)
            s = self.state
            return s
    
        possible_play = self.check_board(board)
        #player two
        selection = random.choice(possible_play)
        board[selection[0]][selection[1]] = 2
        
        c_s = self.state_reg(board)
        self.state.append(c_s)
        
        state_reward, point = self.elvaluate(board, 2)
        if point != 0:
            print("player 2: "+str(state_reward))
            print(self.state)
            s = self.state
            return s
        
        self.play(board, game)

total_games = 3
game = 1
data_set = {}
c = tic_tac_toe()

while game <= total_games:
    board = np.array(np.zeros([3,3], dtype='int'))
    game_data = c.play(board, game)
    print(game_data)
    data_set[game] = game_data
    game += 1

print(data_set)

