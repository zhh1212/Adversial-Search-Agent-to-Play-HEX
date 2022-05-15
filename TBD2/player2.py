from TBD2.help import find_captures, check_winning_condition
from TBD2.astar import a_star
import numpy as np


token = {'red':1, 'blue':2}
opponent = {'red':'blue', 'blue':'red'}

def get_astar_distance(n, start_list, end_list, cells, color):
    distance = []
    for s in start_list:
        for g in end_list:
            if s not in cells[opponent[color]] and g not in cells[opponent[color]]:
                distance.append(a_star(n, s, g,
                    cells[opponent[color]],
                    cells[color]))
    if not distance:
        return 100000
    return min(distance)



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
            self.op_start = [(0, i) for i in range(n)]
            self.op_end = [(n-1, i) for i in range(n)]
        else:
            self.start = [(0, i) for i in range(n)]
            self.end = [(n-1, i) for i in range(n)]
            self.op_start = [(i, 0) for i in range(n)]
            self.op_end = [(i, n-1) for i in range(n)]
        self.n = n
        self.board = np.zeros((n, n), dtype=int) # is this really neccessary?
        # self.own_distance = 100000
        # self.opp_distance = 100000
        self.cells = {'red':[], 'blue': []}
        self.nturns = 0

    def take(self, coord, color):
        self.board[coord[0]][coord[1]] = 0
        self.cells[color].remove(coord)

    def place(self, coord, color):
        self.board[coord[0]][coord[1]] = token[color]
        self.cells[color].append(coord)

    def get_empty_cells(self):
        empty_cells = []
        for i in range(self.n):
            for j in range(self.n):
                if not self.board[i][j]:
                    empty_cells.append((i, j))
        return empty_cells

    def eval_astar_score(self):
        return get_astar_distance(self.n, self.op_start, self.op_end,
                                self.cells, opponent[self.player]) \
                - get_astar_distance(self.n, self.start, self.end,
                                self.cells, self.player)
    def count(self):
        return len(self.cells[self.player]) - len(self.cells[opponent[self.player]])
    
    def alpha_beta_pruning(self, cur_player, depth, alpha, beta):
        # print(self.board)
        best_move = None
        # print(self.player)
        # maybe plus wining condition?
        if depth <= 0 or check_winning_condition(self.board, token[cur_player]):
            # print('here')
            best_score = self.eval_astar_score()
            if cur_player == self.player:
                return best_move, best_score
            else:
                return best_move, best_score
        else:
            possible_moves = self.get_empty_cells()
            if possible_moves:
                if cur_player == self.player:
                    best_score = -100000
                    for move in possible_moves:
                        self.place(move, cur_player)
                        captured_cells = find_captures(self.board, move, token[cur_player], self.n)
                        for c in captured_cells:
                            self.take(c, opponent[cur_player])
                        result = self.alpha_beta_pruning(opponent[cur_player], depth-1, alpha, beta)
                        if result[1] > best_score:
                            best_score = result[1]
                            # 
                            best_move = move
                        alpha = max(alpha, best_score)

                        # recover the board
                        for c in captured_cells:
                            self.place(c, opponent[cur_player])
                        self.take(move, cur_player)
                        if beta <= alpha:
                            break
                    # print(best_score)
                    return best_move, best_score
                else:
                    best_score = 100000
                    for move in possible_moves:

                        self.place(move, cur_player)
                        captured_cells = find_captures(self.board, move, token[cur_player], self.n)
                        for c in captured_cells:
                            self.take(c, opponent[cur_player])
                        result = self.alpha_beta_pruning(opponent[cur_player], depth-1, alpha, beta)
                        if -result[1] < best_score:
                            best_score = -result[1]
                            best_move = move
                        beta = min(beta, best_score)
                        # recover the board
                        for c in captured_cells:
                            self.place(c, opponent[cur_player])
                        self.take(move, cur_player)
                        if beta <= alpha:
                            break
                    # print(best_move)
                    return best_move, best_score

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        result = self.alpha_beta_pruning(self.player, 5, -100000, 100000)
        return('PLACE', result[0][0], result[0][1])

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
            
        # place the token
        self.place(action[1:], player)

        # check if there's any captures and remove them if so
        for c in find_captures(self.board, action[1:], token[player], self.n):
            self.take(c, opponent[player])
        self.nturns += 1
        # print(self.eval_astar_score())
        # print(self.cells)
        # print(self.board)
