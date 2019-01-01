'''
Author: Derek Ly
Question: Route Between Nodes (Pg. 109)
---------------------------------------------------------------------
Given a directed graph, design an algorithm to find out whether there
is a route between two nodes.
---------------------------------------------------------------------
'''

class adjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
