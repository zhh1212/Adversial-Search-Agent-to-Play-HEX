from operator import itemgetter

def cal_distance(goal, p):
    """
    The function is to calculate the expected shortest distance between the cell 'p' and the goal
    When assuming no pieces existing on the initial board
    """
    if (goal[0] >= p[0] and goal[1] >= p[1]) or (goal[0] <= p[0] and goal[1] <= p[1]):
        return abs(goal[0]-p[0]) + abs(goal[1]-p[1])
    else:
        return max(abs(goal[0]-p[0]), abs(goal[1]-p[1]))

# def cal_heu(goal, n, existing_cells):
#     """
#     This function is for helper function to visualise a heuristic board
#     """
#     heu_dict = {}
#     # add blue tokens in as obstacles
#     for cell in existing_cells:
#         heu_dict[cell] = '-'
#     for i in range(n):
#         for j in range(n):
#             # assume we are playing red
#             if (i, j) not in heu_dict:
#                 heu_dict[(i, j)] = cal_distance(goal, (i, j))

#     return heu_dict

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

def a_star(n, start, goal, exist_cells, own_cells):
    """
    Function to implement the A* algorithm
    """
    open_dict = {}
    closed_list = []
    parent_table = {}
    dist_dictionary = {}
    open_dict[start] = 0
    dist_dictionary[start] = 0
    while goal not in open_dict and open_dict:
        current_cell = sorted(open_dict.items(), key=itemgetter(1))[0][0]
        open_dict.pop(current_cell)
        closed_list.append(current_cell)
        current_distance = dist_dictionary[current_cell]
        for neighbor in neighborhood(n, current_cell):
            # print(neighbor)
            # assume we don't use any existing pieces on the board
            if neighbor in closed_list or neighbor in exist_cells:
                continue
            elif neighbor in open_dict and dist_dictionary[neighbor] <= current_distance + 1:
                continue
            
            else:
                parent_table[neighbor] = current_cell
                dist_dictionary[neighbor] = current_distance + 1
                open_dict[neighbor] = cal_distance(goal, neighbor) + dist_dictionary[neighbor]
    # traverse the path
    cell = goal
    # path = []

    # # might be a problem
    shortest_distance = 2
    if goal in own_cells:
        shortest_distance -= 1
    if start in own_cells:
        shortest_distance -= 1
    if not open_dict:
        return 100000
    while open_dict and parent_table[cell] != start:
        # path.append(parent_table[cell])
        # board_dict[parent_table[cell]] = 'r'
        cell = parent_table[cell]
        if cell not in own_cells:
            shortest_distance += 1
    return shortest_distance

