""" data_set dictionery format
    {game_no:{state:[Q-value, reward]}} """
import numpy as np
import random

class tic_tac_toe():
    
    def __init__(self, board):
        self.current_game = {}
        self.board = board
    
    def row(self, player):
        
        for i in range(3):
            w = True
            for j in range(3):
                if self.board[i][j] != player:
                    w = False
            
            return w
            
    def col(self, player):
        
        for i in range(3):
            w = True
            for j in range(3):
                if self.board[j][i] != player:
                    w = False
            
            return w
                
    def diag(self, player):
        
        win = True
        
        for i in range(3): 
            if self.board[i, i] != player: 
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
            
    def elvaluate(self, p):
        
        winner = 0
        p = p
        
        for player in [1, 2]: 
            if (self.row(player) or
                self.col(player) or
                self.diag(player)): 
                winner = player
            
            if np.all(self.board != 0) and winner == 0: 
                winner = -1
    	
        result = self.reward(winner, p)
        return result, winner
        
    
    def check_board(self):
        empty = []
        
        for row in range(len(self.board)):
            for box in range(len(self.board[row])):
                if self.board[row][box] == 0:
                    empty.append([row,box])
    
        return empty
    
    def state_reg(self):
        current_state = []
        for x in self.board:
            for j in range(len(x)):
                current_state.append(x[j])
        return current_state
    
    def play(self, game):
        #Player one
        game = game
        print(self.board)
        possible_play = self.check_board()
        selection = random.choice(possible_play)
        self.board[selection[0]][selection[1]] = 1
        
        c_s = self.state_reg()
        c_s = tuple(c_s)
        self.current_game[c_s] = [0,0]
        
        state_reward, point = self.elvaluate(1)
        if point != 0:
            print("player 1: "+str(state_reward))
#            print(self.state)
            return self.current_game
    
        possible_play = self.check_board()
        #player two
        selection = random.choice(possible_play)
        self.board[selection[0]][selection[1]] = 2
        
        c_s = self.state_reg()
        c_s = tuple(c_s)
        self.current_game[c_s] = [0,0]
        
        state_reward, point = self.elvaluate(2)
        if point != 0:
            print("player 2: "+str(state_reward))
#            print(self.state)
            return self.current_game
        
        return self.play(game)

total_games = 3
game = 1
data_set = {}

while game <= total_games:
    board = np.array(np.zeros([3,3], dtype='int'))
    c = tic_tac_toe(board)
    game_data = c.play(game)
#    print(game_data)
    data_set[game] = game_data
    game += 1
    
print(data_set)



