"""
In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.
"""

from inspect import stack
import time
from xml.dom import NoModificationAllowedErr

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
    queue = []
    discovered = set()
    queue.append(state)
    
    # test_state = ((1, 4, 2), (0, 5, 8), (3, 6, 7))  
    

    total_visited_states = 0
    actionpath=[]

    while queue:
        total_visited_states +=1  
        current_state = queue.pop(0)
        for action, state in get_successors(current_state):
            if state not in discovered:
             queue.append(state)
             discovered.add(state)
             prev[state] = current_state
             actions[state] = action
             if goal_test(state) == True:
                 while state != test_state:
                     if actions[state]=="Up":
                      actionpath.append("Down")
                     elif actions[state]=="Down":
                         actionpath.append("Up")
                     elif actions[state]=="Right":
                         actionpath.append("Left")
                     elif actions[state]=="Left":
                         actionpath.append("Right")
            
                     state=prev[state]

                 actionpath.reverse()
                 print(actionpath)
                 print("Total visited states:", total_visited_states-1) 
                 return actionpath
                 
             
    print("Total visited states:", total_visited_states-1) 
    return None # No solution found

                               
     
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
    stack = []
    discovered = set()
    stack.append(state)
    
    # test_state = ((1, 4, 2), (0, 5, 8), (3, 6, 7))  
    

    total_visited_states = 0
    
    actionpath=[]

    while stack:
        total_visited_states +=1  
        current_state = stack.pop()
        for action, state in get_successors(current_state):
            if state not in discovered:
             stack.append(state)
             discovered.add(state)
             prev[state] = current_state
             actions[state] = action
             
             if goal_test(state) == True:
                 while state != test_state:
                     actionpath.append(actions[state])
                     state=prev[state]
                 actionpath.reverse()
                 print("Total visited states:", total_visited_states-1) 
                 return actionpath 
                 
                 
             
    print("Total visited states:", total_visited_states-1) 
    return None # No solution found

def misplaced_heuristic(state):
    correct = 0
    misplaced = 0
    for j in state:
        for i in j:
            if correct != i and i != 0:
                misplaced += 1
            correct +=1
    
    return misplaced # replace this


def manhattan_heuristic(state):
    correct = 0
    total = 0
    #current row
    j_current = 0
    for j in state:
        #current colum
        i_current = 0
        
        for i in j:
            
            if correct != i and i != 0:
              
              #actual position
               correct_row = i // 3
               correct_column = i % 3
               
               #total calculation
               if j_current > correct_row:
                   j_diff = j_current - correct_row
                   total += j_diff
               elif j_current < correct_row:
                       j_diff = correct_row - j_current
                       total += j_diff
               if i_current > correct_column:
                       i_diff = i_current - correct_column
                       total += i_diff
               elif i_current < correct_column:
                       i_diff = correct_column - i_current 
                       total += i_diff
               

            correct += 1
            i_current += 1
        j_current += 1
    

    return total # replace this


def greedy(state, heuristic = misplaced_heuristic):

  prev = {}
  actions = {} 
  queue = []
  discovered = set()
  queue.append(state)

    # test_state = ((1, 4, 2), (0, 5, 8), (3, 6, 7))  
    

  total_visited_states = 0
    
  actionpath=[]

  while queue:
        total_visited_states +=1  
        current_state = queue.pop()
        successors = get_successors(current_state) 
        successors.sort(key = lambda tup: heuristic(tup[1]), reverse = True)
            
        for action, state in successors:
            if state not in discovered:
             queue.append(state)
             discovered.add(state)
             prev[state] = current_state
             actions[state] = action
             
             if goal_test(state) == True:
                 while state != test_state:
                     actionpath.append(actions[state])
                     state=prev[state]
                 actionpath.reverse()
                 print("Total visited states:", total_visited_states) 
                 return actionpath 
                 
                 
             
  print("Total visited states:", total_visited_states) 
  return None



def best_first(state, heuristic = manhattan_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns: A list of actions
    Shoudl print: the number of states visited, and the maximum size of the frontier.  
    """
    from heapq import heappush
    from heapq import heappop
    
    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there

    # Write code here for bfs.  
    discovered = set()
    
    heap = [(heuristic(state), state)]
    
    # test_state = ((1, 4, 2), (0, 5, 8), (3, 6, 7))  
    

    total_visited_states = 0
    actionpath=[]

    while heap:
        total_visited_states +=1  
        x , current_state = heappop(heap)
        for action, state in get_successors(current_state):
            if state not in discovered:
             heappush(heap,(heuristic(state), state))
             discovered.add(state)
             prev[state] = current_state
             actions[state] = action
             if goal_test(state) == True:
                 
                 while state != test_state:
                     actionpath.append(actions[state])
                      
                     state=prev[state]

                 actionpath.reverse()

                 print("Total visited states:", total_visited_states) 
                 return actionpath
                 
             
    print("Total visited states:", total_visited_states) 
    return None # No solution found

    


def astar(state, heuristic = manhattan_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns: A list of actions
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    from heapq import heappush
    from heapq import heappop

    prev = {}
    actions = {}
    cost = {}

    cost[state] = 0
    
    heap = [(heuristic(state), state)]
    
    discovered = set()
    discovered.add(state)

    total_visited_states = 0
    actionpath=[]

    while heap:
        total_visited_states +=1  
        x , current_state = heappop(heap)
        for action, state in get_successors(current_state):
            if state not in discovered:
             discovered.add(state)
             cost[state] = cost[current_state] + 1
             heappush(heap,(heuristic(state)+cost[state], state))
             
             prev[state] = current_state
             actions[state] = action
             if goal_test(state) == True:
                 
                 while state != test_state:
                     actionpath.append(actions[state])
                      
                     state=prev[state]

                 actionpath.reverse()

                 print("Total visited states:", total_visited_states) 
                 return actionpath
                 
             
    print("Total visited states:", total_visited_states) 
    return None # No solution found


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
    #test_state = ((1, 4, 2),
                  #(0, 5, 8), 
                  #(3, 6, 7))  

    #More difficult test case
    test_state = ((7, 2, 4),
                  (5, 0, 6), 
                  (8, 3, 1))  

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



