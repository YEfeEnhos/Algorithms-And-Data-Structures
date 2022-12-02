"""

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.

"""

import time
from turtle import pen

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True
   
def bfs(state):
    """
    Breadth first search.
    Returns A list of actions
    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there
    # Write code here for bfs.  

    q = [state]

    discovered = set()
    discovered.add(state)

    states_visited = 0 
    max_frontier = 0 

    while q: 

        v = q.pop(0) # VISIT

        states_visited += 1

        for action, u in get_successors(v):  #DISCOVER
            
            if not u in discovered: 
                q.append(u)

                max_frontier = max(max_frontier, len(q))

                discovered.add(u)
                prev[u] = v
                actions[u] = action
                
                if goal_test(u): 
                    # get the action sequence that takes me from u to v
                    print("States visited:", states_visited)
                    print("Max queue size:",max_frontier)
                    return get_path(u, prev, actions)
        
                
    return None# No solution found
                               
#def get_path(state, prev, action):
#    
#    if not state in prev: 
#        return []
#
#    return get_path(prev[state], prev, action) + [action[state]]
    
def get_path(state, prev, action):

    result = []
    while state in prev: 
        result.append(action[state])
        state = prev[state]

    return result[::-1] # reverse the result

    

def dfs(state):
    """
    Depth first search.
    Returns: A list of actions.
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there
    # Write code here for bfs.  

    stack = [state]

    discovered = set()
    discovered.add(state)

    states_visited = 0 
    max_frontier = 0 

    while stack: 

        v = stack.pop() # VISIT

        states_visited += 1

        for action, u in get_successors(v):  #DISCOVER
            
            if not u in discovered: 
                stack.append(u)

                max_frontier = max(max_frontier, len(stack))

                discovered.add(u)
                prev[u] = v
                actions[u] = action
                
                if goal_test(u): 
                    # get the action sequence that takes me from u to v
                    print("States visited:", states_visited)
                    print("Max queue size:",max_frontier)
                    return get_path(u, prev, actions)
        
                
    return None# No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    counter = 0
    misplaced = 0 
    for row in state:
        for cell in row: 
            if counter != cell and cell != 0: 
               misplaced += 1 
            counter += 1
    return misplaced


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """
    counter = 0
    total = 0 
 
    row_idx = 0 
    for row in state:
        column_idx = 0 
        for cell in row: 
            if counter != cell and cell != 0: 
                
               correct_row = cell // 3
               correct_column = cell % 3
               
               total += abs(correct_row - row_idx) + abs(correct_column - column_idx)

            counter += 1
            column_idx += 1
        row_idx += 1

    return total 


def greedy(state, heuristic = misplaced_heuristic):
    """
    Greedy search is a variant of depth-first search that uses a heuristic to 
    select the next state from the immediate successor states.  
    Returns three values: A list of actions.

    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """

    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there
    # Write code here for bfs.  

    stack = [state]

    discovered = set()
    discovered.add(state)

    states_visited = 0 
    max_frontier = 0 

    while stack: 

        v = stack.pop() # VISIT

        states_visited += 1

        successors = get_successors(v) 
        successors.sort(key = lambda tup: heuristic(tup[1]), reverse = True)
    
        for action, u in successors:  #DISCOVER
            
            if not u in discovered: 
                stack.append(u)

                max_frontier = max(max_frontier, len(stack))

                discovered.add(u)
                prev[u] = v
                actions[u] = action
                
                if goal_test(u): 
                    # get the action sequence that takes me from u to v
                    print("States visited:", states_visited)
                    print("Max queue size:",max_frontier)
                    return get_path(u, prev, actions)
        
                
    return None# No solution found


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns: A list of actions
    Shoudl print: the number of states expanded, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there
    # Write code here for bfs.  

    heap = [(heuristic(state), state)]

    discovered = set()
    discovered.add(state)

    states_visited = 0 
    max_frontier = 0 

    while heap: 

        hv, v = heappop(heap) # VISIT

        states_visited += 1

        for action, u in get_successors(v):  #DISCOVER
            
            if not u in discovered: 
                heappush(heap,(heuristic(u), u))

                max_frontier = max(max_frontier, len(heap))

                discovered.add(u)
                prev[u] = v
                actions[u] = action
                
                if goal_test(u): 
                    # get the action sequence that takes me from u to v
                    print("States visited:", states_visited)
                    print("Max queue size:",max_frontier)
                    return get_path(u, prev, actions)
        
                
    return None# No solution found
                               

def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns: A list of actions
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    from heapq import heappush
    from heapq import heappop

    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there
    cost = {}
    # Write code here for bfs.  

    cost[state] = 0

    heap = [(0+heuristic(state), state)]

    discovered = set()
    discovered.add(state)

    states_visited = 0 
    max_frontier = 0 

    while heap: 

        hv, v = heappop(heap) # VISIT

        states_visited += 1

        for action, u in get_successors(v):  #DISCOVER
            
            if not u in discovered: 

                max_frontier = max(max_frontier, len(heap))

                discovered.add(u)
                cost[u] = cost[v] + 1
                heappush(heap,(cost[u]+heuristic(u), u))

                prev[u] = v
                actions[u] = action
                
                if goal_test(u): 
                    # get the action sequence that takes me from u to v
                    print("States visited:", states_visited)
                    print("Max queue size:",max_frontier)
                    return get_path(u, prev, actions)
        
                
    return None# No solution found
                               

def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7))  

    #More difficult test case
    test_state = ((7, 2, 4), (5, 0, 6), (8, 3, 1))  

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    start = time.time()
    solution = bfs(test_state) #
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    print()

    print("====Greedy====") 
    start = time.time()
    solution = greedy(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A*====") 
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))




