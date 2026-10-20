# Terminal Sudoku

A beginner-friendly Sudoku game written in Python. It runs in your terminal and uses only Python's standard library—no extra packages are needed.

## Project files

- `main.py` — the complete game, including puzzle generation, board display, input handling, and Sudoku validation.
- `.gitignore` — common Python-generated files and local environment folders to ignore.

## Requirements

- Python 3.8 or newer (Python 3.10+ is also fine).
- A terminal or command prompt.

## How to run

1. Extract the ZIP file.
2. Open a terminal in the `sudoku` project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## How to play

1. Choose **1. New game** from the menu.
2. The board shows empty cells as dots (`.`). Rows and columns are numbered 1–9.
3. When prompted, enter the row, column, and number you want to place.
4. Enter `0` as the number to clear a cell you filled.
5. The original numbers in the puzzle are fixed and cannot be changed.
6. Type `Q` at any prompt to quit the current game.
7. Choose **2. Rules** from the menu to see the rules, or **3. Quit** to exit.

## Basic Sudoku rules

- Every row must contain numbers 1 through 9 exactly once.
- Every column must contain numbers 1 through 9 exactly once.
- Every 3×3 box must contain numbers 1 through 9 exactly once.

This game generates a completed valid Sudoku board, removes cells to make a puzzle, and checks your entries against its solution. It removes 42 cells per puzzle, which is a simple fixed difficulty setting.

## Practise Git and GitHub

This ZIP intentionally does **not** include a `.git` folder or an initialized Git repository. You can practise setting one up yourself:

```bash
git init
git status
git add .
git commit -m "Initial Sudoku game"
```

To connect it to GitHub, create an empty repository on GitHub and follow GitHub's instructions for adding the remote and pushing your first commit.
