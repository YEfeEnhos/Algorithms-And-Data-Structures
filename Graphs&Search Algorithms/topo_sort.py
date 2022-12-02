graph = {"A" : ["B","C","G"],
         "B" : ["C","D"],
         "C" : ["E"],
         "D" : ["E"],
         "E" : ["F"],
         "F" : ["G"],
         "G" : []}

def topo_sort(graph):
    
    indegrees = {}
    for s in graph: 
        indegrees[s] = 0
    for s in graph: 
        for t in graph[s]:
            indegrees[t] += 1
    
    queue = []
    output = []
    for s in indegrees: 
        if indegrees[s] == 0:
            queue.append(s)
            
    while queue: 
        s = queue.pop(0)
        output.append(s)
        for t in graph[s]:
            indegrees[t] -= 1
            if indegrees[t] == 0:
                queue.append(t)
    return output

print(topo_sort(graph))
