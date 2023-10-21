# Python3 program to print BFS traversal from a given source vertex. BFS(init s) traverses vertices reachable from s. 

from collections import defaultdict

# This class represents a directed graph using adjacency list representation. 

class Graph: # Declare a new class for a graph

# Constructor
    def __init__(self): # Declare the constructor for the class 

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph
        # Make a list visited[] to rcheck if a node is already visited or not. 
        def addEdge(self,u,v): 
            self.graph[u].append(v)
            self.visited=[]

