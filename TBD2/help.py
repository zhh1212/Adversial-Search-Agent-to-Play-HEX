import numpy as np

_SWAP_PLAYER = {1: 2, 2: 1}
_ADD = lambda a, b: (a[0] + b[0], a[1] + b[1])
_HEX_STEPS = np.array([(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)], dtype='i,i')
_CAPTURE_PATTERNS = [[_ADD(n1, n2), n1, n2] 
    for n1, n2 in 
        list(zip(_HEX_STEPS, np.roll(_HEX_STEPS, 1))) + 
        list(zip(_HEX_STEPS, np.roll(_HEX_STEPS, 2)))]

def inside_bounds(coord, n):
    r, q = coord
    return r >= 0 and r < n and q >= 0 and q < n

def find_captures(board, coord, opp_type, n):
        """
        Check coord for diamond captures, and apply these to the board
        if they exist. Returns a list of captured token coordinates.
        """
        mid_type = _SWAP_PLAYER[opp_type]
        captured = set()

        # Check each capture pattern intersecting with coord
        for pattern in _CAPTURE_PATTERNS:
            coords = [_ADD(coord, s) for s in pattern]
            # No point checking if any coord is outside the board!
            if all(map(inside_bounds, coords, [n]*3)):
                tokens = [board[coord[0]][coord[1]] for coord in coords]
                if tokens == [opp_type, mid_type, mid_type]:
                    # Capturing has to be deferred in case of overlaps
                    # Both mid cell tokens should be captured
                    captured.update(coords[1:])
        
        return list(captured)