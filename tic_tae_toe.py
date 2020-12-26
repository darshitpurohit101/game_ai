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
            if w == True:
    #            print("row: ",board)
    #            print("w: ",w)
                return w
            
    def col(self, player):
        
        for i in range(3):
            w = True
            for j in range(3):
                if self.board[j][i] != player:
                    w = False
            if w == True:
                return w
                
    def diag(self,player):
        
        win = True
        d1 = [[0,0],[1,1],[2,2]]
        d1 = np.array(d1)
        d2 = [[0,2],[1,1],[2,0]]
        d2 = np.array(d2)
        
        for i in range(len(d1)): 
            if self.board[d1[i,0], d1[i,1]] != player: 
                win = False
        
        if win == False:
                    
            for i in range(len(d2)): 
                if self.board[d2[i, 0], d2[i,1]] != player: 
                    win = False
                     
        return win 
        
    def reward(self, winner, p):
        
        if winner == 0:
            return 0
        elif winner == p:
            return 1
        elif winner == -1:
            return 1
        else:
            return -1
            
    def elvaluate(self,p):
        
        winner = 0
        p = p
         
        if (self.row(p) or
            self.col(p) or
            self.diag(p)): 
            winner = p
        
        elif np.all(board != 0) and winner == 0: 
            winner = -1
    	
        result = self.reward(winner, 2)
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
    
    def action(self, positions, player):
        
        selection = random.choice(positions)
        self.board[selection[0]][selection[1]] = player
        
    
    def play(self, game):
        #Players [1,2]
        game = game
        for p in iter([1,2]):
#            print(self.board)
            possible_play = self.check_board()
            self.action(possible_play, p)
    
            c_s = self.state_reg()
            c_s = tuple(c_s)
            self.current_game[c_s] = [0,0]
        
            state_reward, point = self.elvaluate(p)
            if point != 0:
                print("player 2: "+str(state_reward))
                print(self.board)
                #print(self.state)
                return self.current_game
            print(self.board)
            print("/n")
        
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



