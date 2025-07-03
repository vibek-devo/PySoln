import itertools

def travelling_salesman(graph, start):
    n = len(graph)
    min_path = None
    min_cost = float('inf')

    vertices = list(range(n))
    vertices.remove(start)

    for perm in itertools.permutations(vertices):
        current_cost = 0
        current_path = [start] + list(perm) + [start]
        
        for i in range(len(current_path) - 1):
            u = current_path[i]
            v = current_path[i + 1]
            current_cost += graph[u][v]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path

    return min_path, min_cost

# Example usage
n = int(input("Enter number of cities: "))
print("Enter the cost matrix (use 999999 or a high number for no direct path):")

graph = []
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    graph.append(row)

start = int(input("Enter starting city index (0 to {}): ".format(n-1)))

path, cost = travelling_salesman(graph, start)
print("\nMinimum cost path:", ' -> '.join(map(str, path)))
print("Total cost:", cost)















# Enter number of cities: 4
# Enter the cost matrix:
# Row 1: 0 10 15 20
# Row 2: 10 0 35 25
# Row 3: 15 35 0 30
# Row 4: 20 25 30 0
# Enter starting city index (0 to 3): 0
