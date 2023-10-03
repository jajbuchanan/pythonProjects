from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # A queue to keep track of nodes to be visited

    while queue: 
        vertex = queue.popleft()  # Dequeue a vertex from queue
        if vertex not in visited: 
            print(vertex, end=" ")  # Print the current vertex
            visited.add(vertex)  # Mark the vertex as visited


            # Add unvisited neighbors to the queue

            for neighbor in graph[vertex]:
                if neighbor not in visited: 
                    queue.append(neighbor)


# Test the function with a sample graph

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'], 
        'D': ['B'], 
        'E': ['B', 'H'], 
        'F': ['C'], 
        'G': ['C'], 
        'H': ['E']
    }

print("Breadth First Traversal starting from vertex: A")
bfs(graph, 'A')
