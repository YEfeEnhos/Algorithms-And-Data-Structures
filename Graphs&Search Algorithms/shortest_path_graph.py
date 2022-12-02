graph = {'A': ['B','C'],
 'B': ['A','D','C'],
 'C': ['A','B','D','E'], 
 'D': ['B','C','E','F'],
 'F': ['D','E'],
 'E': ['C','D','F']}

visited = [] 
queue = []     
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for elem in graph[s]:
      if elem not in visited:
        visited.append(elem)
        queue.append(elem)
        

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
   
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
  
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)

        path_index += 1

    
    return []

def unweighted_shortest_path(graph, node):
      cost = {}
      
      for val in graph:
            cost[val] = 0

      q = []
      discovered = set()
      
      q.append(node)
      discovered.add(node)
      
      while q:
            v = q.pop(0)
            for w in graph[v]:
                  if w not in discovered:
                        discovered.add(w)
                        cost[w] = cost[v]+1
                        q.append(w)
      
      return cost

def unweighted_shortest_path2(graph, node1, node2):
  
   
      path_list = [node2]
  
      previous = {}

            
      q = []
      discovered = set()
      
      q.append(node1)
      discovered.add(node1)
      
      while q:
            v = q.pop(0)
            for w in graph[v]:
                  if w not in discovered:
                        discovered.add(w)
                        previous[w] = v
                        
                        q.append(w)
                        if node2 in discovered:
                              q = []

                        
      while True:
            if path_list[0] == node1:
                  break
            path_list.insert(0, previous[path_list[0]])

      return path_list

print(bfs(visited, graph, 'A'))
print(shortest_path(graph, "A","D"))
print(unweighted_shortest_path(graph, "A"))
print(unweighted_shortest_path2(graph, "A", "D"))
