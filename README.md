# The Cachex AI
- An AI using the advesrial search techniques to play the game Cachex

# What is Cachex?
- Cachex is a variation of the traditional (https://en.wikipedia.org/wiki/Hex_(board_game)#Game_play)<a href="https://en.wikipedia.org/wiki/Hex_(board_game)#Game_play">&nbsp;Hex board game</a> which is a perfect-information two-player game played on an n × n rhombic, hexagonally tiled board, with the goal to form a connection between the opposing sides of the board corresponding to their respective color.
- Cachex has also got the following additional rules being implemented when playing:
    - Red will always play first and starting with a hex in the center is **illegal**
    - To mitigate first-mover advantage, the **swap(pie) rule** applies. Once Red completes their first move, Blue may choose to proceed as normal and lay down a blue stone, or steal Red’s move for their own, reflecting the position of Red’s stone along the major axis of symmetry (i.e. interchanging the row and column index) and changing the stone from red to blue. The game proceeds as normal, with Red playing next.
    -  Pairs of tokens may be removed from the game through a **capture mechanism** If a 2 × 2 symmetric1 diamond of cells is formed consisting of two stones from Red and Blue each, the player who completed the diamond removes their opponent’s stones from the game (see the image below). Note that:
        - Either player may exploit the capture rule, and the capture rule applies for all possible
        orientations of the diamond found on the gameboard.
        - The capture mechanism only applies to a diamond formed by 2 Red and 2 Blue stones -
        it does not apply if there are three of one color and one of the other.
        - If multiple diamonds of valid type are formed by placement of a single stone on the
        board, all of the opponent’s stones in the just-formed diamonds are removed from the
        board.
        - After a capture, the opposing party can immediately threaten a re-capture by placing a
        piece on one of the recently-captured positions.
[<src="img/cap.png">]
# Report Link:
- 

# Dependencies:
- All you need is Python 3(or above) with the library 'NumPy' been installedd

# How to run the program?:
- 