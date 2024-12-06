from board import Board
from player import Player

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = []

    def setup_players(self):
        """Sets up the two players."""
        name1 = input("Enter Player 1's name: ")
        name2 = input("Enter Player 2's name: ")
        self.players = [
            Player(name1, "X"),
            Player(name2, "O")
        ]

    def play(self):
        """Main game loop."""
        print("Welcome to Tic Tac Toe!")
        print("Use the numbers 1-9 to make your move:")
        self.board.display()

        current_player_idx = 0
        while True:
            current_player = self.players[current_player_idx]
            self.board.display()

            # Get and process the move
            row, col = current_player.get_move()
            if self.board.update(row, col, current_player.symbol):
                # Check for win or draw
                if self.board.check_winner(current_player.symbol):
                    self.board.display()
                    print(f"Congratulations, {current_player.name}! You win!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    break

                # Switch players
                current_player_idx = 1 - current_player_idx
            else:
                print("Cell already taken. Please choose a different move.")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.setup_players()
    game.play()
