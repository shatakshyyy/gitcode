class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

# Define a pathNode class to store the path from source to destination
class pathNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

# Define a function to add edges to the graph
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight
    adj[u].append(Node(v, weight))

# Define the GBFS algorithm function
def GBFS(h, V, src, dest):
    """ 
    This function returns a list of 
    integers that denote the shortest
    path found using the GBFS algorithm.
    If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList
    openList = []
    closeList = []

    # Inserting src in openList
    openList.append(pathNode(src, None))

    # Iterating while the openList is not empty
    while openList:
        # Finding the node with the least 'h' value
        currentNode = min(openList, key=lambda x: h[x.node])

        # Removing the currentNode from the openList and adding it in the closeList
        openList.remove(currentNode)
        closeList.append(currentNode)

        # If we have reached the destination node
        if currentNode.node == dest:
            # Initializing the 'path' list 
            path = []
            cur = currentNode

            # Adding all the nodes in the path list through which we have
            # reached to dest.
            while cur:
                path.append(cur.node)
                cur = cur.parent

            # Reversing the path, because currently it denotes path from dest to src
            path.reverse()
            return path

        # Iterating over adjacents of 'currentNode'
        # and adding them to openList if they are neither in openList nor closeList
        for node in adj[currentNode.node]:
            if any(node.v == x.node for x in openList):
                continue
            if any(node.v == x.node for x in closeList):
                continue
            openList.append(pathNode(node.v, currentNode))

    return []

# Define the adjacency list
adj = [[] for i in range(10)]

# Make the graph
addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)

# Define the heuristic values for each node
h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]

# Find the shortest path using the GBFS algorithm
path = GBFS(h, 10, 0, 9)

# Print the path
for i in range(len(path) - 1):
    print(path[i], end = " -> ")
print(path[-1])