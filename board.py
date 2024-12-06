class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        """Displays the current board."""
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def is_full(self):
        """Checks if the board is full (draw condition)."""
        return all(cell != " " for row in self.board for cell in row)

    def update(self, row, col, player):
        """Updates the board with the player's move."""
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def check_winner(self, player):
        """Checks if the given player has won."""
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
