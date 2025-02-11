# 🧩 Number Merge Quest – A Python Board Game

This project is a Python-based number board game where players collect matching adjacent cells to clear the grid and earn points. The game dynamically updates the board after each move and follows strategic rules for merging and collapsing cells.

## 📌 Features
- **Dynamic Number Board:** The game board is read from an input file and randomly generated.
- **Cell Matching Mechanism:** Players can select a cell, and all adjacent cells with the same value disappear.
- **Board Collapse Logic:** Columns shift down when cells are removed, and empty columns shift left.
- **Scoring System:** The score is calculated based on the number of cells removed and their value.
- **Error Handling:** Prevents invalid moves and provides feedback.

Run the game using the following command:
   ```bash
   python3 assignment3.py input.txt
