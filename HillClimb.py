import random

# Objective function (you can change this)
def objective_function(x):
    return -1 * (x ** 2) + 4 * x  # This has a peak at x = 2

# Hill Climbing Algorithm
def hill_climb(start, step_size, max_iterations):
    current_x = start
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        # Try a small move to the left and right
        neighbors = [current_x + step_size, current_x - step_size]
        next_x = None
        next_value = current_value

        for x in neighbors:
            value = objective_function(x)
            if value > next_value:
                next_x = x
                next_value = value

        # If no improvement, stop
        if next_x is None:
            break

        current_x = next_x
        current_value = next_value

    return current_x, current_value

# User input interface
def main():
    print("Hill Climbing Algorithm")
    try:
        start = float(input("Enter starting point (e.g., 0): "))
        step_size = float(input("Enter step size (e.g., 0.1): "))
        max_iter = int(input("Enter max iterations (e.g., 100): "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    best_x, best_val = hill_climb(start, step_size, max_iter)

    print(f"\nBest solution found:")
    print(f"x = {best_x:.4f}, f(x) = {best_val:.4f}")

if __name__ == "__main__":
    main()
