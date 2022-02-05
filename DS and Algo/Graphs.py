# Graph representation is used when the tree fails. It is fast and also stores the path.
# Graph are circular means we can go back to the node if they are connected.
# Graph has "EDGES" and "VERTICES".

## Here to make a graph, we will use dictionary implementation ##

class Graph:
    def __init__(self, gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict

    def addEdge(self, vertex, edge):
        self.gDict[vertex].append(edge)

    def bfs(self, vertex): # O(V+E) - TIME & SPACE COMPLEXITY of "BREADTH FIRST SEARCH"
        visited = [vertex]
        queue= [vertex]
        while queue is not None: # O(V) - time , V= no. of vertex
            deQVertex = queue.pop(0)
            print(deQVertex)
            for adjacentVertex in self.gDict[deQVertex]: # O(E) - Time, E = number of edges
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self,vertex): # O(V+E) - space and time complexity
        visited = [vertex]
        stack = [vertex]
        while stack: # O(V)
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gDict[popVertex]: # O(E) 
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex )

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f"],
            "f" : ["d", "e"]
               }

newGraph = Graph(customDict)
newGraph.dfs("a")



