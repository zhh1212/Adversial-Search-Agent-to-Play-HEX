import imp
from TBD2.help import find_captures, check_winning_condition
from TBD2.astar import a_star
from TBD2.statetable import TranspositionTable
import numpy as np


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
        self.opponent = opponent[player]
        self.edge = {'red': ([(0, i) for i in range(n)], [(n-1, i) for i in range(n)]),
                    'blue': ([(i, 0) for i in range(n)], [(i, n-1) for i in range(n)])}
        self.n = n
        self.board = np.zeros((n, n), dtype=int) 
        # self.own_distance = 100000
        # self.opp_distance = 100000
        self.cells = {'red':[], 'blue': []}
        self.nturns = 0
        self.depth = 0
        self.state_table = TranspositionTable()

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
    
    def get_astar_distance(self, color):
        distance = []
        for s in self.edge[color][0]:
            for g in self.edge[color][1]:
                if s not in self.cells[opponent[color]] and g not in self.cells[opponent[color]]:
                    distance.append(a_star(self.n, s, g,
                        self.cells[opponent[color]],
                        self.cells[color]))
        if not distance:
            return 100000
      
        return min(distance)

    def eval_astar_score(self):
        return self.get_astar_distance(self.opponent) - self.get_astar_distance(self.player)
    def count(self):
        return len(self.cells[self.player]) - len(self.cells[self.opponent])
    
    def alpha_beta_pruning(self, cur_player, depth, alpha, beta):
        # print(self.cells)
        # print(self.board, cur_player, self.eval_astar_score(),
            #  self.get_astar_distance(self.opponent), self.get_astar_distance(self.player))
        # print(self.edge[opponent[cur_player]][1])
        # print('\n')
        
        # print(check_winning_condition(self.board, token[opponent[cur_player]]))
        best_move = None
        hit, state_move, state_score = self.state_table.lookup(depth, self.board.tostring()) 
        # if actual best move at passed depth has been foun
        if hit == 2: 
            return state_move, state_score
        if depth <= 0:
            # print('here')
            best_score = self.count()
            # print(best_score, '\n\n')
            return best_move, best_score
        if (self.nturns + self.depth - depth >= 2*self.n-1 and check_winning_condition(self.board, token[opponent[cur_player]])):
            if cur_player == self.opponent:
                return best_move, 100000
            else:
                return best_move, -100000
        else:
            possible_moves = self.get_empty_cells()
            if cur_player == self.player:
                best_score = -100000
                for move in possible_moves:
                    self.place(move, cur_player)
                    captured_cells = find_captures(self.board, move, token[cur_player], self.n)
                    for c in captured_cells:
                        self.take(c, opponent[cur_player])
                    result = self.alpha_beta_pruning(opponent[cur_player], depth-1, alpha, beta)
                    # print('abc', result[1])
                    if result[1] > best_score:
                        best_score = result[1]
                        # 
                        # print('hhh',best_score)
                        # print(self.board, '\n')
                        best_move = move
                    alpha = max(alpha, best_score)
                    # recover the board
                    for c in captured_cells:
                        self.place(c, opponent[cur_player])
                    self.take(move, cur_player)
                    if beta <= alpha:
                        break
                # print(best_score)
                self.state_table.store(depth, self.board.tostring(), best_move, best_score)
                return best_move, best_score
            else:
                best_score = 100000
                for move in possible_moves:
                    self.place(move, cur_player)
                    captured_cells = find_captures(self.board, move, token[cur_player], self.n)
                    for c in captured_cells:
                        self.take(c, opponent[cur_player])
                    result = self.alpha_beta_pruning(opponent[cur_player], depth-1, alpha, beta)
                    if result[1] < best_score:
                        best_score = result[1]
                        # print('ttt',best_score)
                        best_move = move
                    beta = min(beta, best_score)
                    # recover the board
                    for c in captured_cells:
                        self.place(c, opponent[cur_player])
                    self.take(move, cur_player)
                    if beta <= alpha:
                        break
                # print(best_move)
                self.state_table.store(depth, self.board.tostring(), best_move, best_score)
                return best_move, best_score
    
    def get_greedy(self):
        best_dist = self.n * self.n
        best_move = (self.n - 1, self.n - 1)
        print(self.board)
        for move in self.get_empty_cells():
                self.place(move, self.player)
                captured_cells = find_captures(self.board, move, token[self.player], self.n)
                for c in captured_cells:
                    self.take(c, opponent[self.player])

                shortest_dist = self.n * self.n
                for i in range(self.n):
                    for j in range(self.n):
                        if self.player == "red":
                            dist = a_star(self.n, (0, i), (self.n-1, j),
                                self.cells[self.opponent], self.cells[self.player])
                        else:
                            dist = a_star(self.n, (i, 0), (j, self.n-1),
                                self.cells[self.opponent], self.cells[self.player])
                        # print("dist = ", dist)
                        if dist < shortest_dist:
                            shortest_dist = dist
                # update best move 
                if shortest_dist < best_dist:
                    best_move = move
                    best_dist = shortest_dist

                # recover the board
                for c in captured_cells:
                        self.place(c, self.opponent)
                self.take(move, self.player)
        # print(self.board)
        return ("PLACE", best_move[0], best_move[1])

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        if self.nturns == 1:
            return('STEAL',)

        n_exist_cells = len(self.cells[self.player]) + len(self.cells[self.opponent])
        if self.n <= 5:
            self.depth = 8 - self.n
        elif n_exist_cells/(self.n**2) <= 0.3:
            self.depth = 1
        elif n_exist_cells/(self.n**2) > 0.3 and n_exist_cells/(self.n**2) <= 0.6:
            self.depth = 2
        elif n_exist_cells/(self.n**2) > 0.6 and n_exist_cells/(self.n**2) <= 0.8:
            self.depth = 3
        else:
            self.depth = 4

        if self.depth == 0:
            return self.get_greedy()
        else:
            result = self.alpha_beta_pruning(self.player, self.depth, -100000, 100000)
        # if self.nturns==5:
            # return ('hhh')
            if not result[0]:
                return self.get_greedy()
            else:
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
        # if self.nturns <= 2*self.n - 1:
        #     self.depth = self.depth / 2
        # else:
        #     self.depth = self.depth * 2
        
        # if steal
        if action[0] == 'STEAL':
            cell = self.cells[opponent[player]][0]
            self.take(cell, opponent[player])
            # implement steal the cells about the symmetry
            self.place((cell[1], cell[0]), player)
            self.nturns += 1
            if self.nturns % (self.n) == 0 and self.nturns != 0:
                self.depth += 1
        # place the token
        else:
            self.place(action[1:], player)

            # check if there's any captures and remove them if so
            for c in find_captures(self.board, action[1:], token[player], self.n):
                self.take(c, opponent[player])
            self.nturns += 1
            
            # print(self.cells[player])
            # print(self.get_astar_distance(player))
            # print(self.get_astar_distance(opponent[player]))
            # print('\n', self.eval_astar_score(), '\n')
            # print(self.cells)
            # print(self.board)
        # print(self.board)
        # print(self.nturns)