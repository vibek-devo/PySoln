import heapq

# Goal state for reference
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Get the Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Find position of zero (blank)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible next moves
def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Check if states are equal
def states_equal(a, b):
    return all(a[i][j] == b[i][j] for i in range(3) for j in range(3))

# Convert state to a tuple (hashable for sets)
def state_to_tuple(state):
    return tuple([num for row in state for num in row])

# A* algorithm
def a_star(start):
    visited = set()
    queue = []
    heapq.heappush(queue, (manhattan_distance(start), 0, start, []))

    while queue:
        est_cost, cost, current, path = heapq.heappop(queue)

        if states_equal(current, goal_state):
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(queue, (priority, new_cost, neighbor, path + [current]))

    return None

# Pretty print
def print_state(state):
    for row in state:
        print(' '.join(str(num) if num != 0 else ' ' for num in row))
    print()

# Main function with user input
def main():
    print("Enter the 8-puzzle start state row by row (use 0 for the blank):")
    start_state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1} (e.g. 1 2 3): ").split()))
        start_state.append(row)

    print("\nSolving...\n")
    solution = a_star(start_state)

    if solution:
        print(f"Solution found in {len(solution)-1} moves:")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
















# Enter the 8-puzzle start state row by row (use 0 for the blank):
# Row 1 (e.g. 1 2 3): 1 2 3
# Row 2 (e.g. 4 5 6): 4 0 6
# Row 3 (e.g. 7 8 0): 7 5 8
