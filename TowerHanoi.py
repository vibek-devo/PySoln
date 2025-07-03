def hanoi(n, source, auxiliary, target, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n-1, source, target, auxiliary, moves)
        moves.append(f"Move disk {n} from {source} to {target}")
        hanoi(n-1, auxiliary, source, target, moves)

def main():
    print("Towers of Hanoi Problem Solver")
    try:
        n = int(input("Enter number of disks: "))
        if n < 1:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    moves = []
    hanoi(n, 'A', 'B', 'C', moves)

    print(f"\nTotal moves required: {len(moves)}\n")
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()
