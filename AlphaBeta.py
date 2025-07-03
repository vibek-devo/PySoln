import math

# Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta):
    # If we are at leaf node (depth 3 => 8 leaf nodes)
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):  # Each node has 2 children
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):  # Each node has 2 children
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

# User Input Function
def main():
    print("Alpha-Beta Pruning Example")
    print("This builds a minimax tree of depth 3 with 8 leaf nodes.")

    try:
        values = list(map(int, input("Enter 8 space-separated leaf node values: ").split()))
        if len(values) != 8:
            print("❌ Error: You must enter exactly 8 values.")
            return
    except ValueError:
        print("❌ Error: Please enter valid integers.")
        return

    optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
    print(f"\n✅ Optimal value (root node): {optimal_value}")

if __name__ == "__main__":
    main()


















#  3 5 6 9 1 2 0 -1