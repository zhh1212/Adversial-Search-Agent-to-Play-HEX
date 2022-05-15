from random import randint
import numpy as np
from TBD2.help import find_captures


token = {'red':1, 'blue':2}
opponent = {'red':'blue', 'blue':'red'}




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
        self.n = n
        self.board = np.zeros((n, n), dtype=int) # is this really neccessary?
        # self.own_distance = 100000
        # self.opp_distance = 100000
        self.cells = {'red':[], 'blue': []}

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here
        # action = [(2,0), (1,2), (1,1)]
        # for i in action:
        #     if not self.board[i[0]][i[1]]:
        #         return ("PLACE", i[0], i[1])
        # implement minimax?
        while True:
            i = randint(0, self.n-1)
            j = randint(0, self.n-1)
            if not self.board[i][j]:
                return ("PLACE", i, j)
    def take(self, coord, color):
        self.board[coord[0]][coord[1]] = 0
        self.cells[color].remove(coord)

    def place(self, coord, color):
        self.board[coord[0]][coord[1]] = token[color]
        self.cells[color].append(coord)

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
        if action[0] == 'STEAL':
            cell = self.cells[opponent[player]][0]
            self.take(cell, opponent[player])
            self.place(cell, player)
        # place the token
        else:
            self.place(action[1:], player)

            # check if there's any captures and remove them if so
            for c in find_captures(self.board, action[1:], token[player], self.n):
                self.take(c, opponent[player])
            # print(self.get_astar_distance(player))
            # print(self.get_astar_distance(opponent[player]))
            # print('\n', self.eval_astar_score(), '\n')
            # print(self.cells)
            # print(self.board)