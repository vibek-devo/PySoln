import math
import random

# Objective function (you can customize this)
def objective_function(x):
    return x**2 + 4 * math.sin(5 * x) + math.sin(20 * x)

# Simulated Annealing algorithm
def simulated_annealing(objective, bounds, temp, cooling_rate, max_iter):
    current_x = random.uniform(bounds[0], bounds[1])
    current_energy = objective(current_x)
    best_x = current_x
    best_energy = current_energy

    for i in range(max_iter):
        candidate_x = current_x + random.uniform(-0.1, 0.1)
        candidate_x = max(min(candidate_x, bounds[1]), bounds[0])  # stay within bounds
        candidate_energy = objective(candidate_x)

        # Energy difference
        delta_e = candidate_energy - current_energy

        # Accept or reject
        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            current_x = candidate_x
            current_energy = candidate_energy

            if current_energy < best_energy:
                best_x = current_x
                best_energy = current_energy

        temp *= cooling_rate  # cool down

    return best_x, best_energy

# Get user input
def main():
    print("Simulated Annealing Optimization")

    lower_bound = float(input("Enter lower bound (e.g. -5): "))
    upper_bound = float(input("Enter upper bound (e.g. 5): "))
    initial_temp = float(input("Enter initial temperature (e.g. 100): "))
    cooling_rate = float(input("Enter cooling rate (e.g. 0.95): "))
    iterations = int(input("Enter number of iterations (e.g. 1000): "))

    best_solution, best_value = simulated_annealing(
        objective_function,
        bounds=(lower_bound, upper_bound),
        temp=initial_temp,
        cooling_rate=cooling_rate,
        max_iter=iterations
    )

    print(f"\nBest solution: x = {best_solution:.4f}")
    print(f"Best objective value: f(x) = {best_value:.4f}")

if __name__ == "__main__":
    main()
