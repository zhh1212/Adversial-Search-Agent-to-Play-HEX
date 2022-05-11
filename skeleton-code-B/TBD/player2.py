from referee.board import Board

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
                if not Board.is_occupied(self, (i, j)):
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

