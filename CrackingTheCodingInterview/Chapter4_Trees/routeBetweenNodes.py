'''
Author: Derek Ly
Question: Route Between Nodes (Pg. 109)
---------------------------------------------------------------------
Given a directed graph, design an algorithm to find out whether there
is a route between two nodes.
---------------------------------------------------------------------
'''

'''
Standard Graph Class
'''

class Graph:
    def __init__(self, graphDict = None):
        # If no graph is provided, then set initial graph to be a dictionary
        if graphDict == None:
            graphDict = {}

        self.graph = graphDict

    def vertices(self):
        return list(self.graph.keys())

    def findAllEdges(self):
        edges = []

        for vertice in self.graph:
            for edge in self.graph[vertice]:
                if {edge, vertice} not in edges:
                    edges.append({vertice, edge})

        return edges

    def edges(self):
        return self.findAllEdges()

'''
Function routeBetweenNodes
--------------------------

This function will use recursion to solve the path problem. Given a graph,
starting node and ending node, the function will iterate through the keys
in graph and check for every key that might have a connection to the final
node.

This method uses DFS to traverse through all of the vertices connected to
the first vertice. Another method would be to use BFS.
'''

def routeBetweenNodes(graph, nodeA, nodeB, path = None):

    if path == None:
        path = []

    g = graph

    path = path + [nodeA]

    # Check if we're on that node already
    if nodeA == nodeB:
        return path

    if nodeA not in g:
        return None

    # Traverse through every vertice in graph
    # and check for connected paths
    for vertice in g[nodeA]:
        if vertice not in path:
            conPath = routeBetweenNodes(graph, vertice, nodeB, path)

            if conPath:
                return conPath

    return None



'''
Test cases
'''

testGraph = { "a" : ["b", "c"],
              "b" : ["d"],
              "c" : ["e"],
              "d" : ["f"],
              "e" : ["f"],
              "f" : []
}

'''
This test case should print out:

a -> b -> d -> f
'''
graph = Graph(testGraph)
path = routeBetweenNodes(graph.graph, "a", "f")
print(path)
