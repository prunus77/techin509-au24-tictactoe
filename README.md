### README for Tic Tac Toe Game

---

# Tic Tac Toe Game

Welcome to the **Tic Tac Toe Game**, a simple text-based game implemented in Python. This project uses **Object-Oriented Programming (OOP)** principles and is structured into multiple files for better modularity and maintainability.

---

## Features

- **Two-player Mode:** Play against another person locally.
- **Interactive Gameplay:** Players take turns choosing their moves by entering positions (1-9).
- **Winning Conditions:** The game detects a win, loss, or draw.
- **Clear Board Display:** The board is updated in real-time and displayed after every move.
- **Modular Design:** The game logic is divided into multiple files (`Board`, `Player`, `Game`) for clarity and reusability.

---

## Folder Structure

```
tic_tac_toe/
│
├── __init__.py     # Package initializer
├── board.py        # Board-related functionality
├── player.py       # Player-related functionality
└── game.py         # Main game logic
```

---

## Prerequisites

- Python 3.6 or later installed on your system.
- Basic knowledge of how to run Python scripts.

---

## How to Run the Game

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd tic_tac_toe
   ```

2. **Run the Game:**
   ```bash
   python game.py
   ```

3. **Follow the On-Screen Instructions:**
   - Enter player names when prompted.
   - Use numbers (1-9) to make moves based on the following layout:

      ```
       1 | 2 | 3
      -----------
       4 | 5 | 6
      -----------
       7 | 8 | 9
      ```

   - The game ends with a winner or a draw message.

---

## Classes and Design

### 1. **Board Class (`board.py`)**
   - Manages the game board.
   - Provides methods to display the board, update moves, and check for wins/draws.

### 2. **Player Class (`player.py`)**
   - Represents each player.
   - Handles player-specific information like name, symbol, and move input.

### 3. **TicTacToe Class (`game.py`)**
   - Orchestrates the game flow.
   - Sets up players, manages turns, and determines game outcomes.
   - The other classes are called in this class

### 4. **Initialization Class (`__init__.py`)**
   - Forms the base of the OOP 
   - This file initializes all files together
---

## Example Gameplay

```
Welcome to Tic Tac Toe!
Player X goes first.
Use the numbers 1-9 to make your move:

Player 1 (X), enter your move (1-9): 5
   |   |  
-----------
   | X |  
-----------
   |   |  

Player 2 (O), enter your move (1-9): 1
 O |   |  
-----------
   | X |  
-----------
   |   |  
```

---

## Citations

# Used ChatGPT to structure this data but I have added my own comments and learnigs especially in the information about the files and classes.
