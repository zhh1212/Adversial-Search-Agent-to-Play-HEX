from TBD2.help import find_captures
from TBD2.astar import a_star
import numpy as np


token = {'red':1, 'blue':2}
opponent = {'red':'blue', 'blue':'red'}

# def alpha_beta_minimax(state, player, depth=3, alpha, beta):


class Player:
    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        self.player = player
        if self.player == 'blue':
            self.start = [(i, 0) for i in range(n)]
            self.end = [(i, n-1) for i in range(n)]
        else:
            self.start = [(0, i) for i in range(n)]
            self.end = [(n-1, i) for i in range(n)]
        self.n = n
        self.board = np.zeros((n, n), dtype=int)
        self.own_distance = 100000
        self.opp_distance = 100000
        self.cells = {'red':[], 'blue': []}


    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
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
        
        # if steal
        
        # place the token
        self.board[action[1]][action[2]] = token[player]
        # 
        self.cells[player].append(action[1:])
        # check if there's any captures and remove them if so
        for c in find_captures(self.board, action[1:], token[player], self.n):
            self.board[c[0]][c[1]] = 0
            self.cells[opponent[player]].remove(c)
        distance = []
        for s in self.start:
            for g in self.end:
                distance.append(a_star(self.n,s,g, 
                    self.cells[opponent[player]],
                    self.cells[player]))
        print(distance)
        # print(self.cells)
        # print(self.board)
