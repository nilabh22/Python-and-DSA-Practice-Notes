#  Single source shortest path problem (SSSPP) is about finding a path from a given vertex to all the vertex ....
#  ....such that the distance between them (source and destination) is minimum

# BFS for SSSPP
# BFS does not work for Weighted graph.
# DFS will not work for SSSPP because , it has the tendency to go as deep as possibl. Hence, it can fail in proving Shortest path


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end): # O(E) - not O(V+E) because, in bfs for SSSPP, we are only visiting the connected vertices. If we have any isolated..
        queue = [] # ...vertex we will not visit it
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customDict = {"a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"],
              "e": ["f"],
              "g": ["f"]
              }

g = Graph(customDict)
print(g.bfs("a", "e"))