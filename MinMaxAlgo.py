import math

class TicTacToe:
    def __init__(self):
        # Initialize empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.human = 'X'
        self.ai = 'O'
        
    def print_board(self):
        """Print the current state of the board"""
        print("  0 1 2")
        for i in range(3):
            print(f"{i} {self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}")
            if i < 2:
                print("  -+-+-")
    
    def is_valid_move(self, row, col):
        """Check if a move is valid"""
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        if self.board[row][col] != ' ':
            return False
        return True
    
    def make_move(self, row, col, player):
        """Make a move on the board"""
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner or a tie"""
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        
        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Check for tie
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Tie'
        
        # Game still ongoing
        return None
    
    def get_available_moves(self):
        """Get all empty cells"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        """
        Minimax algorithm with alpha-beta pruning
        
        Parameters:
        - depth: current depth in the game tree
        - is_maximizing: True if current move is by maximizing player (AI)
        - alpha, beta: parameters for alpha-beta pruning
        
        Returns:
        - best score for the current board state
        """
        result = self.check_winner()
        
        # Terminal states
        if result == self.ai:
            return 10 - depth  # AI wins (higher score for quicker wins)
        elif result == self.human:
            return depth - 10  # Human wins (lower score)
        elif result == 'Tie':
            return 0  # Tie
        
        if is_maximizing:
            # AI's turn (maximizing)
            best_score = float('-inf')
            for move in self.get_available_moves():
                row, col = move
                self.board[row][col] = self.ai
                score = self.minimax(depth + 1, False, alpha, beta)
                self.board[row][col] = ' '  # Undo move
                best_score = max(score, best_score)
                
                # Alpha-beta pruning
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            # Human's turn (minimizing)
            best_score = float('inf')
            for move in self.get_available_moves():
                row, col = move
                self.board[row][col] = self.human
                score = self.minimax(depth + 1, True, alpha, beta)
                self.board[row][col] = ' '  # Undo move
                best_score = min(score, best_score)
                
                # Alpha-beta pruning
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
    
    def best_move(self):
        """Find the best move for AI using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        
        for move in self.get_available_moves():
            row, col = move
            self.board[row][col] = self.ai
            score = self.minimax(0, False)
            self.board[row][col] = ' '  # Undo move
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def play_game(self):
        """Main game loop"""
        print("Welcome to Tic-Tac-Toe!")
        print("You are X, the computer is O")
        
        # Determine who goes first
        turn = input("Do you want to go first? (y/n): ").lower()
        current_player = self.human if turn == 'y' else self.ai
        
        while True:
            self.print_board()
            
            # Check for game end
            result = self.check_winner()
            if result:
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {result} wins!")
                break
            
            if current_player == self.human:
                # Human's turn
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row (0-2): "))
                        col = int(input("Enter column (0-2): "))
                        valid_move = self.make_move(row, col, self.human)
                        if not valid_move:
                            print("Invalid move, try again.")
                    except ValueError:
                        print("Please enter numbers between 0-2.")
                current_player = self.ai
            else:
                # AI's turn
                print("Computer is thinking...")
                row, col = self.best_move()
                print(f"Computer chose: row {row}, column {col}")
                self.make_move(row, col, self.ai)
                current_player = self.human
        
        # Show final board
        self.print_board()
        print("Game over!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()