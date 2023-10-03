from collections import deque

def bfs_path(graph, start, end):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([(start, [start])])  # A queue to keep track of nodes to be visited

    while queue: 
        (vertex, path) = queue.popleft()  # Dequeue a vertex from queue
        if vertex not in visited: 
            visited.add(vertex)  # Mark the vertex as visited


            # Add unvisited neighbors to the queue

            for neighbor in graph[vertex]:
                if neighbor == end: 
                    return path + [neighbor] # Return path when end is found
                if neighbor not in visited: 
                    queue.append((neighbor, path + [neighbor]))
    return None # Path not found


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

print("Path from A to H:")
print(bfs_path(graph, 'A', 'H'))
