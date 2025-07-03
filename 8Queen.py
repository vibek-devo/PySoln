def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += "Q " if board[i][j] else ". "
        print(row)
    print("\n")

def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Found a solution
        solutions.append([row.copy() for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def main():
    print("N-Queens Problem Solver")
    n = int(input("Enter number of queens (e.g., 8): "))
    
    if n < 1 or n > 20:
        print("Please enter a number between 1 and 20.")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    if not solutions:
        print("No solution found.")
    else:
        print(f"\nTotal solutions found: {len(solutions)}")
        print("\nShowing the first solution:\n")
        print_board(solutions[0], n)

if __name__ == "__main__":
    main()
