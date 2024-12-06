# Tic Tac Toe Game

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """Checks if the current player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    """Gets the player's move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return divmod(move, 3)
            else:
                print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("Player X goes first.")
    print("Use the numbers 1-9 to make your move:")
    print_board([[str(i + 1) for i in range(3 * j, 3 * j + 3)] for j in range(3)])

    # Players take turns
    current_player = "X"
    while True:
        print_board(board)
        row, col = get_move(current_player)

        # Check if the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player

            # Check for winner or draw
            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Choose another move.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
