
from TBD.astar import a_star, capture
import numpy as np

class Player:
    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        # put your code here
        self.self = self
        self.player = player
        self.n = n
        self.board = []
        self.first_turn = True
                
        for i in range(self.n):
            lst = [0] * self.n
            self.board.append(lst)
                
        # print(self.board)  
        
    
            

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here
        
        # implement minimax?
        
        # start with simple implementation
        # for i in range(self.n):
        #     for j in range(self.n):
        #         if not self.board[i][j]:
        #             return ("PLACE", i, j)
        
        # fist turn
        if self.first_turn == True:
            self.first_turn = False
            if self.player == "red":
                return ("PLACE", 0, 0)
            else:
                return ("STEAL",)
            
                
        # implement greedy approach
        # find A* for all possible boards
        possible_moves = {}
        for i in range(self.n):
            for j in range(self.n):
                new_board = np.copy(self.board)
 
                if self.board[i][j] == 0:
                    if self.player == "red":
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 2
                    possible_moves[str(i) + str(j)] = capture(new_board, self.n, i, j, self.player)
                    
        # print("possible_moves = ", possible_moves.keys())
        # find shortest A* path, place based on that path
        best_dist = self.n * self.n
        best_move = (self.n - 1, self.n - 1)
        for move in possible_moves.keys():
            own_cells = []
            exist_cells = []
            board = possible_moves[move]
            r = move[0]
            q = move[1]
            for i in range(self.n):
                for j in range(self.n):
                    if ( board[i][j] == 1 and self.player == "red" ) or ( board[i][j] == 2 and self.player == "blue" ):
                        own_cells.append((i,j))
                    elif ( board[i][j] == 1 and self.player == "blue" ) or ( board[i][j] == 2 and self.player == "red" ):
                        exist_cells.append((i,j))
            # print("own_cells = ", own_cells)
            # print("exist_cells = ", exist_cells)
            
            shortest_dist = self.n * self.n
            for i in range(self.n):
                for j in range(self.n):
                    if self.player == "red":
                        dist = a_star(self.n, (0,i), (self.n-1, j), exist_cells, own_cells)
                    else:
                        dist = a_star(self.n, (i,0), (j, self.n-1), exist_cells, own_cells)
                    # print("dist = ", dist)
                    if dist < shortest_dist:
                        shortest_dist = dist
                    
            # update best move       
            if shortest_dist < best_dist:
                best_move = (int(r), int(q))
                best_dist = shortest_dist
                
        return ("PLACE", best_move[0], best_move[1])
                
        
                
                
                
    
    def turn(self, player, action):
        """
        Called at the end of each player's turn to inform this player of 
        their chosen action. Update your internal representation of the 
        game state based on this. The parameter action is the chosen 
        action itself. 
        
        Note: At the end of your player's turn, the action parameter is
        the same as what your player returned from the action method
        above. However, the referee has validated it at this point.
        """
        if action[0] == "STEAL":
            # find prev move
            for i in range(self.n):
                for j in range(self.n):
                    if self.board[i][j] != 0:
                        self.board[i][j] = 2
        else:
        
            new_board = np.copy(self.board)
            if player == "red":
                new_board[action[1]][action[2]] = 1
            else:
                new_board[action[1]][action[2]] = 2
            self.board = capture(new_board, self.n, action[1], action[2], player)