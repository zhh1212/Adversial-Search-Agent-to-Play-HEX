class Player:
    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        self.nturns = 0
        

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        if self.nturns == 1:
            m_type = input('Choose the move type (STEAL/PLACE): ')
            if m_type == "STEAL":
                return ("STEAL",)
            elif m_type == "PLACE":
                r = input("Choose the cell row: ")
                q = input("Choose the cell column: ")
                return("PLACE", int(r), int(q))
            else:
                print("invalid move type")
        else:
            r = input("Choose the cell row: ")
            q = input("Choose the cell column: ")
            return("PLACE", int(r), int(q))
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
        self.nturns += 1