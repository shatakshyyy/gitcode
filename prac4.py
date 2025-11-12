graph = {
    '5': ['3', '7'], 
    '3' : ['2', '4'], 
    '7': ['8'], 
    '2' :[], 
    '4': ['8'], 
    '8': []
    }

queue = []
visited = []

def bfs(visited, graph, node):
     queue.append(node)
     visited.append(node)

     while queue:
          m = queue.pop(0)
          print(m, end = " ")

          for neigbour in graph[m]:
               if neigbour not in visited:
                    queue.append(neigbour)
                    visited.append(neigbour)

print("the traversed list")
bfs(visited, graph, '5')
