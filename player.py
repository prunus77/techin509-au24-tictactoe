class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        """Prompts the player to input their move."""
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): ")) - 1
                if 0 <= move <= 8:
                    return divmod(move, 3)  # Convert to row, col
                else:
                    print("Invalid input. Please choose a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
