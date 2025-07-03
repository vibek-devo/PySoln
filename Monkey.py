from collections import deque

# Check if goal is reached
def is_goal(state):
    return state["monkey"] == "on_box" and state["box_pos"] == state["banana_pos"]

# Generate possible actions
def get_successors(state):
    successors = []
    monkey = state["monkey"]
    box_pos = state["box_pos"]
    monkey_pos = state["monkey_pos"]
    banana_pos = state["banana_pos"]

    if monkey == "on_floor":
        # Move monkey
        for pos in ["left", "middle", "right"]:
            if pos != monkey_pos:
                successors.append({
                    "monkey": "on_floor",
                    "monkey_pos": pos,
                    "box_pos": box_pos,
                    "banana_pos": banana_pos,
                    "action": f"Monkey moves to {pos}"
                })

        # Push box (only if monkey and box are at the same position)
        if monkey_pos == box_pos:
            for pos in ["left", "middle", "right"]:
                if pos != box_pos:
                    successors.append({
                        "monkey": "on_floor",
                        "monkey_pos": pos,
                        "box_pos": pos,
                        "banana_pos": banana_pos,
                        "action": f"Monkey pushes box to {pos}"
                    })

        # Climb box
        if monkey_pos == box_pos:
            successors.append({
                "monkey": "on_box",
                "monkey_pos": monkey_pos,
                "box_pos": box_pos,
                "banana_pos": banana_pos,
                "action": "Monkey climbs the box"
            })

    elif monkey == "on_box":
        if box_pos == banana_pos:
            successors.append({
                "monkey": "on_box",
                "monkey_pos": monkey_pos,
                "box_pos": box_pos,
                "banana_pos": banana_pos,
                "action": "Monkey grabs the banana "
            })

    return successors

# Breadth-First Search to solve the problem
def bfs_monkey_problem(initial_state):
    visited = set()
    queue = deque()
    path_map = {}

    def state_key(s):
        return (s["monkey"], s["monkey_pos"], s["box_pos"])

    queue.append(initial_state)
    visited.add(state_key(initial_state))
    path_map[state_key(initial_state)] = []

    while queue:
        current = queue.popleft()

        if is_goal(current):
            return path_map[state_key(current)] + [current["action"]]

        for successor in get_successors(current):
            key = state_key(successor)
            if key not in visited:
                visited.add(key)
                queue.append(successor)
                path_map[key] = path_map[state_key(current)] + [successor["action"]]

    return None

# Main Program
def main():
    print(" Monkey and Banana Problem Solver")
    print("Positions: left, middle, right")

    monkey_pos = input("Enter monkey's starting position: ").strip().lower()
    box_pos = input("Enter box's position: ").strip().lower()
    banana_pos = input("Enter banana's position: ").strip().lower()

    # Validate positions
    valid_positions = {"left", "middle", "right"}
    if monkey_pos not in valid_positions or box_pos not in valid_positions or banana_pos not in valid_positions:
        print(" Invalid position entered. Please use left, middle, or right.")
        return

    initial_state = {
        "monkey": "on_floor",
        "monkey_pos": monkey_pos,
        "box_pos": box_pos,
        "banana_pos": banana_pos,
        "action": "Start"
    }

    solution = bfs_monkey_problem(initial_state)

    if solution:
        print("\n Solution found:")
        for step in solution:
            print("-->", step)
    else:
        print(" No solution found.")

if __name__ == "__main__":
    main()
