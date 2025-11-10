from queue import PriorityQueue

# ----- Graph Representation -----
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# ----- Heuristic values (estimated cost to goal) -----
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

# ----- Best First Search -----
def best_first_search(start, goal):
    print("\n--- Best First Search ---")
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    visited = set()

    while not pq.empty():
        _, node = pq.get()
        print(node, end=' ')
        if node == goal:
            print("\nGoal reached!")
            return
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                pq.put((heuristic[neighbour], neighbour))


# ----- A* Search -----
def a_star(start, goal):
    print("\n--- A* Search ---")
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    g_cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        f, node = pq.get()
        print(node, end=' ')
        if node == goal:
            print("\nGoal reached!")
            reconstruct_path(parent, start, goal)
            return

        for neighbour, cost in graph[node].items():
            new_g = g_cost[node] + cost
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                f_new = new_g + heuristic[neighbour]
                pq.put((f_new, neighbour))
                parent[neighbour] = node


# ----- Reconstruct path (used by A*) -----
def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    print("Optimal Path:", " -> ".join(path))


# ----- Main Code -----
if __name__ == "__main__":
    print("Graph Nodes and Edges:")
    for node, edges in graph.items():
        print(f"{node} -> {edges}")

    best_first_search('A', 'G')
    a_star('A', 'G')
