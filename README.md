# 💎 Marble Betting Game Simulation

This project is a command-line simulation of a simple gambling game where the player bets virtual currency (Gold Pieces) on the outcome of drawing a marble from a bag. The simulation is written in Python and is designed to run until a specified number of rounds is completed or the player loses half of their starting money.

## 🕹️ Game Rules and Features

### Core Rules
* **Starting Gold:** The player begins with **1,000 Gold Pieces**.
* **Goal:** The game continues for the number of rounds specified by the player, or until the player's gold balance drops to **500 or less** (losing half their starting capital), resulting in an immediate **Game Over**.
* **Betting:** The player must enter a valid bet amount before each round. The system validates that the bet is positive, a whole number, and that the player has sufficient funds.
* **Replacement:** Marbles are **replaced** into the bag after every draw, ensuring the odds remain consistent.

## 🚀 How to Run the Simulation

### Prerequisites
You need **Python 3** installed on your system.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd marble-betting-game
    ```
3.  **Run the Script:**
    ```bash
    python your_script_name.py
    ```
    *(Note: Replace `your_script_name.py` with the actual name of your Python file.)*

## 💡 Key Code Implementation Details

* **Robust Input Handling:** The script uses **`try...except ValueError`** blocks to prevent the program from crashing if a user enters non-numeric text for rounds or bets.
* **Game Loop Control:** The main game loop is controlled by the user-defined round count and an immediate `break` if the gold balance triggers the "lose half" condition.
* **Randomness:** The `random.choice()` function is used to ensure the marble draw is fair and adheres to the specified odds.

## 📝 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
