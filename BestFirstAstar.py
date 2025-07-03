import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    queue = [(heuristics[start], start, [start])]

    while queue:
        h, current, path = heapq.heappop(queue)
        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor, cost in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

def a_star_search(graph, heuristics, start, goal):
    visited = set()
    queue = [(heuristics[start], 0, start, [start])]  # (f = g + h, g, node, path)

    while queue:
        f, g, current, path = heapq.heappop(queue)
        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor, cost in graph[current]:
                if neighbor not in visited:
                    g_new = g + cost
                    f_new = g_new + heuristics[neighbor]
                    heapq.heappush(queue, (f_new, g_new, neighbor, path + [neighbor]))

    return None

# User Input Function
def build_graph():
    graph = {}
    heuristics = {}

    n = int(input("Enter number of nodes (e.g., 5): "))
    for _ in range(n):
        node = input("Enter node name: ")
        heuristics[node] = float(input(f"Heuristic value (to goal) for {node}: "))
        graph[node] = []

    m = int(input("Enter number of edges: "))
    for _ in range(m):
        src = input("From node: ")
        dest = input("To node: ")
        cost = float(input(f"Cost from {src} to {dest}: "))
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))  # undirected graph

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    return graph, heuristics, start, goal

# Main Function
def main():
    print("Best-First Search and A* Algorithm for Pathfinding")
    graph, heuristics, start, goal = build_graph()

    print("\n--- Best-First Search Result ---")
    path_bfs = best_first_search(graph, heuristics, start, goal)
    if path_bfs:
        print("Path found:", " -> ".join(path_bfs))
    else:
        print("No path found.")

    print("\n--- A* Search Result ---")
    path_astar = a_star_search(graph, heuristics, start, goal)
    if path_astar:
        print("Path found:", " -> ".join(path_astar))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()


















# Enter number of nodes: 5
# Enter node name: A
# Heuristic: 10
# Enter node name: B
# Heuristic: 6
# Enter node name: C
# Heuristic: 4
# Enter node name: D
# Heuristic: 2
# Enter node name: G
# Heuristic: 0

# Enter number of edges: 6
# From node: A
# To node: B
# Cost: 1
# From node: A
# To node: C
# Cost: 4
# From node: B
# To node: D
# Cost: 5
# From node: C
# To node: D
# Cost: 1
# From node: D
# To node: G
# Cost: 3
# From node: B
# To node: G
# Cost: 12

# Enter start node: A
# Enter goal node: G
