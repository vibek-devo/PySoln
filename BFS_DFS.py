from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
n = int(input("Enter number of edges: "))
print("Enter edges (e.g., '0 1'):")

for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)  

start_node = int(input("Enter starting node: "))

print("\nDFS traversal:")
g.dfs(start_node)

print("\nBFS traversal:")
g.bfs(start_node)


















# Enter number of edges: 5
# Enter edges:
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# Enter starting node: 0