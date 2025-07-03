from collections import deque

def is_goal(state, target):
    return target in state

def get_successors(x, y, max_x, max_y):
    return set([
        (0, y),           # Empty Jug X
        (x, 0),           # Empty Jug Y
        (max_x, y),       # Fill Jug X
        (x, max_y),       # Fill Jug Y
        (max_x if x + y > max_x else x + y, y - (max_x - x) if x + y > max_x else 0),  # Pour Y -> X
        (x - (max_y - y) if x + y > max_y else 0, max_y if x + y > max_y else x + y),  # Pour X -> Y
    ])

def bfs_water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    path = {}

    start = (0, 0)
    queue.append(start)
    visited.add(start)
    path[start] = []

    while queue:
        current = queue.popleft()
        x, y = current

        if is_goal(current, target):
            return path[current] + [current]

        for successor in get_successors(x, y, jug1, jug2):
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
                path[successor] = path[current] + [current]

    return None

# Main function with user input
def main():
    print("Water Jug Problem Solver (Using BFS)")

    try:
        jug1 = int(input("Enter capacity of Jug 1: "))
        jug2 = int(input("Enter capacity of Jug 2: "))
        target = int(input("Enter the target amount to measure: "))

        if target > max(jug1, jug2):
            print("❌ Target can't be more than both jug capacities.")
            return
    except ValueError:
        print("❌ Please enter valid integers.")
        return

    solution = bfs_water_jug(jug1, jug2, target)

    if solution:
        print("\n✅ Solution steps:")
        for step in solution:
            print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
        print(f"\n🎯 Reached target {target}L!")
    else:
        print("❌ No solution found.")

if __name__ == "__main__":
    main()
