# Simple Graph Traversal using DFS and BFS

# Create a graph using dictionary (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# ----- Depth First Search (DFS) -----
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()       # To keep track of visited nodes
    print(start, end=' ')     # Visit current node
    visited.add(start)
    for neighbour in graph[start]:  # Visit all unvisited neighbours
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# ----- Breadth First Search (BFS) -----
def bfs(graph, start):
    visited = []             # List to keep track of visited nodes
    queue = []               # List used as a queue
    visited.append(start)
    queue.append(start)

    while queue:             # Run until queue becomes empty
        node = queue.pop(0)  # Remove first node
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# ---- Main Code ----
print("DFS Traversal (starting from A):")
dfs(graph, 'A')

print("\n\nBFS Traversal (starting from A):")
bfs(graph, 'A')
