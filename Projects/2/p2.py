from state import State

initial_state = list()

moves = list()
costs = set()



def move(state, position):

    new_state = state[:]

    index = new_state.index(0)

    if position == 1:  # Up

        if index not in range(0, board_side):

            temp = new_state[index - board_side]
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down

        if index not in range(board_len - board_side, board_len):

            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left

        if index not in range(0, board_len, board_side):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right

        if index not in range(board_side - 1, board_len, board_side):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None


def h(state):

    return sum(abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, board_len)))


def backtrace():

    current_node = goal_node

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves


def export(frontier, time):

    global moves

    moves = backtrace()

    file = open('output.txt', 'w')
    file.write("path_to_goal: " + str(moves))
    file.write("\ncost_of_path: " + str(len(moves)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nfringe_size: " + str(len(frontier)))
    file.write("\nmax_fringe_size: " + str(max_frontier_size))
    file.write("\nsearch_depth: " + str(goal_node.depth))
    file.write("\nmax_search_depth: " + str(max_search_depth))
    file.write("\nrunning_time: " + format(time, '.8f'))
    file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.8f'))    
    file.close()




def main():
    fileIn = open('input.txt', 'r')
    board_height = fileIn.readline()    #n
    board_length = fileIn.readline()    #m
    mario_start = fileIn.readline()
    mushroom_amount = fileIn.readline() #k
    kTmp = mushroom_amount
    mushroom_points_red = list()
    for x in range(0,kTmp):
        mushroom_points_red.append(fileIn.read(1), fileIn.read(2))
    mushroom_points_blue = list()
    for x in range(0,kTmp):
        mushroom_points_blue.append(fileIn.read(1), fileIn.read(2))
    block_points = list()
    while 1:
        block_points.append(fileIn.readline(), fileIn.readline())

    

if __name__ == '__main__':
    main()
