# Wumpus World simple simulator with DFS search
def is_valid(x, y, size):
    return 0 <= x < size and 0 <= y < size

def dfs(world, x, y, visited, path):
    if not is_valid(x, y, len(world)) or (x, y) in visited:
        return False
    if world[x][y] in ['P', 'W']:  # Pit or Wumpus
        return False
    visited.add((x, y))
    path.append((x, y))
    if world[x][y] == 'G':  # Found gold
        return True
    # Explore in all directions: up, down, left, right
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        if dfs(world, x+dx, y+dy, visited, path):
            return True
    path.pop()
    return False

def print_world(world):
    for row in world:
        print(' '.join(row))

def main():
    size = int(input("Enter grid size (e.g., 4 for 4x4): "))
    print("Enter grid values row by row using:")
    print("E for Empty, P for Pit, W for Wumpus, G for Gold")
    print("Example row: E E P E")

    world = []
    for i in range(size):
        row = input(f"Enter row {i+1}: ").strip().split()
        world.append(row)

    print("\nInitial World:")
    print_world(world)

    visited = set()
    path = []
    found = dfs(world, 0, 0, visited, path)

    if found:
        print("\nPath to gold found!")
        for step in path:
            print("->", step)
    else:
        print("\nNo safe path to gold found.")

if __name__ == "__main__":
    main()
















# Enter grid size (e.g., 4 for 4x4): 4
# Enter row 1: E E P E
# Enter row 2: W E P E
# Enter row 3: E E E E
# Enter row 4: P E G E


# Path to gold found!
# -> (0, 0)
# -> (0, 1)
# -> (1, 1)
# -> (2, 1)
# -> (3, 1)
# -> (3, 2)