

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
                
        for i in range(self.n):
            lst = [0] * self.n
            self.board.append(lst)
                
        print(self.board)
        
    def neighborhood(n, cell):
        """
        Function to find all the neighbours of the cell
        """
        neighbors = []
        if cell[0] + 1 < n:
            neighbors.append((cell[0]+1, cell[1]))
            if cell[1] - 1 >= 0:
                neighbors.append((cell[0]+1, cell[1]-1))
        if cell[0] - 1 >= 0:
            neighbors.append((cell[0]-1, cell[1]))
            if cell[1] + 1 < n:
                neighbors.append((cell[0]-1, cell[1]+1))
        if cell[1] + 1 < n:
            neighbors.append((cell[0], cell[1]+1))
        if cell[1] - 1 >= 0:
            neighbors.append((cell[0], cell[1]-1))
        return neighbors
            

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here
        
        # implement minimax?
        
        # start with simple implementation
        for i in range(self.n):
            for j in range(self.n):
                if not self.board[i][j]:
                    return ("PLACE", i, j)
    
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
        
        # put your code here
        if player == "red":
            self.board[action[1]][action[2]] = 1
            
            # check if capture has occured
            
            
            r = action[1]
            q = action[2]
            # start with top left neighboor
            if q > 0 and r+2 < self.n:
                if self.board[r+1][q-1] == 2:
                    if self.board[r+1][q] == 2:
                        if self.board[r+2][q-1] == 1:
                            self.board[r+1][q-1] = 0
                            self.board[r+1][q] = 0
            # then top right neighboor
            if r+1 < self.n and q+1 < self.n:
                if self.board[r+1][q] == 2:
                    if self.board[r][q+1] == 2:
                        if self.board[r+1][q+1] == 1:
                            self.board[r+1][q] = 0
                            self.board[r][q+1] = 0
            # etc
            if q+2 < self.n and r > 0:
                if self.board[r][q+1] == 2:
                    if self.board[r-1][q+1] == 2:
                        if self.board[r-1][q+2] == 1:
                            self.board[r][q+1] = 0
                            self.board[r-1][q+1] = 0
            if r-1 > 0 and q+1 < self.n:
                if self.board[r-1][q+1] == 2:
                    if self.board[r-1][q] == 2:
                        if self.board[r-2][q+1] == 1:
                            self.board[r-1][q+1] = 0
                            self.board[r-1][q] = 0  
            if r > 0 and q > 0 and q+1 < self.n:  
                if self.board[r-1][q] == 2:
                    if self.board[r][q-1] == 2:
                        if self.board[r-1][q-1] == 1:
                            self.board[r-1][q] = 0
                            self.board[r][q-1] = 0
            if q-1 > 0 and r+1 < self.n and q+1 < self.n:
                if self.board[r][q-1] == 2:
                    if self.board[r+1][q-1] == 2:
                        if self.board[r+1][q-2] == 1:
                            self.board[r][q-1] = 0
                            self.board[r+1][q-1] = 0   
                            
            # now check other type of take
            if r+1 < self.n and q > 0 and q+1 < self.n:
                if self.board[r+1][q-1] == 2:
                    if self.board[r+1][q] == 1:
                        if self.board[r][q+1] == 2:
                            self.board[r+1][q-1] = 0
                            self.board[r][q+1] = 0
            if r+1 < self.n and r > 0 and q+1 < self.n:
                if self.board[r+1][q] == 2:
                    if self.board[r][q+1] == 1:
                        if self.board[r-1][q+1] == 2:
                            self.board[r+1][q] = 0
                            self.board[r-1][q+1] = 0
            if r > 0 and q+1 < self.n:
                if self.board[r][q+1] == 2:
                    if self.board[r-1][q+1] == 1:
                        if self.board[r-1][q] == 2:
                            self.board[r][q+1] = 0
                            self.board[r-1][q] = 0
            if q > 0 and r > 0 and q+1 < self.n:
                if self.board[r-1][q+1] == 2:
                    if self.board[r-1][q] == 1:
                        if self.board[r][q-1] == 2:
                            self.board[r-1][q+1] = 0
                            self.board[r][q-1] = 0
            if r > 0 and r+1 < self.n and q > 0:
                if self.board[r-1][q] == 2:
                    if self.board[r][q-1] == 1:
                        if self.board[r+1][q-1] == 2:
                            self.board[r-1][q] = 0
                            self.board[r+1][q-1] = 0
            if q > 0 and r > 0 and q+1 < self.n:
                if self.board[r][q-1] == 2:
                    if self.board[r+1][q-1] == 1:
                        if self.board[r+1][q] == 2:
                            self.board[r][q-1] = 0
                            self.board[r+1][q] = 0
                            
                    
            
            
            
        else:
            self.board[action[1]][action[2]] = 2
            
            r = action[1]
            q = action[2]
            # start with top left neighboor
            if q > 0 and r+2 < self.n:
                if self.board[r+1][q-1] == 1:
                    if self.board[r+1][q] == 1:
                        if self.board[r+2][q-1] == 2:
                            self.board[r+1][q-1] = 0
                            self.board[r+1][q] = 0
            # then top right neighboor
            if r+1 < self.n and q+1 < self.n:
                if self.board[r+1][q] == 1:
                    if self.board[r][q+1] == 1:
                        if self.board[r+1][q+1] == 2:
                            self.board[r+1][q] = 0
                            self.board[r][q+1] = 0
            # etc
            if q+2 < self.n and r > 0:
                if self.board[r][q+1] == 1:
                    if self.board[r-1][q+1] == 1:
                        if self.board[r-1][q+2] == 2:
                            self.board[r][q+1] = 0
                            self.board[r-1][q+1] = 0
            if r-1 > 0 and q+1 < self.n:
                if self.board[r-1][q+1] == 1:
                    if self.board[r-1][q] == 1:
                        if self.board[r-2][q+1] == 2:
                            self.board[r-1][q+1] = 0
                            self.board[r-1][q] = 0   
            if r > 0 and q > 0 and q+1 < self.n:   
                if self.board[r-1][q] == 1:
                    if self.board[r][q-1] == 1:
                        if self.board[r-1][q-1] == 2:
                            self.board[r-1][q] = 0
                            self.board[r][q-1] = 0
            if q-1 > 0 and r+1 < self.n and q+1 < self.n:
                if self.board[r][q-1] == 1:
                    if self.board[r+1][q-1] == 1:
                        if self.board[r+1][q-2] == 2:
                            self.board[r][q-1] = 0
                            self.board[r+1][q-1] = 0   
                            
            # now check other type of take
            if r+1 < self.n and q > 0 and q+1 < self.n:
                if self.board[r+1][q-1] == 1:
                    if self.board[r+1][q] == 2:
                        if self.board[r][q+1] == 1:
                            self.board[r+1][q-1] = 0
                            self.board[r][q+1] = 0
            if r+1 < self.n and r > 0 and q+1 < self.n:
                if self.board[r+1][q] == 1:
                    if self.board[r][q+1] == 2:
                        if self.board[r-1][q+1] == 1:
                            self.board[r+1][q] = 0
                            self.board[r-1][q+1] = 0
            if r > 0 and q+1 < self.n:
                if self.board[r][q+1] == 1:
                    if self.board[r-1][q+1] == 2:
                        if self.board[r-1][q] == 1:
                            self.board[r][q+1] = 0
                            self.board[r-1][q] = 0
            if q > 0 and r > 0 and q+1 < self.n:
                if self.board[r-1][q+1] == 1:
                    if self.board[r-1][q] == 2:
                        if self.board[r][q-1] == 1:
                            self.board[r-1][q+1] = 0
                            self.board[r][q-1] = 0
            if r > 0 and r+1 < self.n and q > 0:
                if self.board[r-1][q] == 1:
                    if self.board[r][q-1] == 2:
                        if self.board[r+1][q-1] == 1:
                            self.board[r-1][q] = 0
                            self.board[r+1][q-1] = 0
            if q > 0 and r > 0 and q+1 < self.n:
                if self.board[r][q-1] == 1:
                    if self.board[r+1][q-1] == 2:
                        if self.board[r+1][q] == 1:
                            self.board[r][q-1] = 0
                            self.board[r+1][q] = 0
            
                    
