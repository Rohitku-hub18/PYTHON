"""
A beginner-friendly terminal Sudoku game.

Run with: python main.py
No external libraries are required.
"""

import random

SIZE = 9
BOX_SIZE = 3
EMPTY = 0


def print_board(board):
    """Display the Sudoku board in a readable grid."""
    print("\n    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")
    for row_index, row in enumerate(board):
        cells = []
        for col_index, value in enumerate(row):
            cells.append(str(value) if value != EMPTY else ".")
            if col_index in (2, 5):
                cells.append("|")
        print(f"{row_index + 1} | " + " ".join(cells) + " |")
        if row_index in (2, 5, 8):
            print("  +-------+-------+-------+")
        else:
            print("  |       |       |       |")
    print()


def is_valid(board, row, col, number):
    """Return True if number can be placed at this position."""
    # Check the row.
    if number in board[row]:
        return False

    # Check the column.
    for row_index in range(SIZE):
        if board[row_index][col] == number:
            return False

    # Check the 3x3 box.
    box_row_start = (row // BOX_SIZE) * BOX_SIZE
    box_col_start = (col // BOX_SIZE) * BOX_SIZE
    for row_index in range(box_row_start, box_row_start + BOX_SIZE):
        for col_index in range(box_col_start, box_col_start + BOX_SIZE):
            if board[row_index][col_index] == number:
                return False

    return True


def solve_board(board):
    """Solve a Sudoku board using simple backtracking."""
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                for number in range(1, SIZE + 1):
                    if is_valid(board, row, col, number):
                        board[row][col] = number
                        if solve_board(board):
                            return True
                        board[row][col] = EMPTY
                return False
    return True


def make_puzzle():
    """Create a new Sudoku puzzle by generating a solved board and removing cells."""
    board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

    # Fill the board with a valid completed Sudoku.
    numbers = list(range(1, SIZE + 1))

    def fill_board():
        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] == EMPTY:
                    random.shuffle(numbers)
                    for number in numbers:
                        if is_valid(board, row, col, number):
                            board[row][col] = number
                            if fill_board():
                                return True
                            board[row][col] = EMPTY
                    return False
        return True

    fill_board()
    solution = [row[:] for row in board]

    # Remove cells to make the puzzle. More blanks means a harder puzzle.
    cells_to_remove = 42
    positions = [(row, col) for row in range(SIZE) for col in range(SIZE)]
    random.shuffle(positions)
    for row, col in positions[:cells_to_remove]:
        board[row][col] = EMPTY

    return board, solution


def is_completed(board):
    """Check whether the player has filled every cell."""
    return all(value != EMPTY for row in board for value in row)


def get_integer(prompt, minimum, maximum):
    """Ask for an integer in a given range, or return None to cancel."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("q", "quit", "exit"):
            return None
        try:
            value = int(answer)
        except ValueError:
            print(f"Please enter a number from {minimum} to {maximum}, or Q to quit.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Please enter a number from {minimum} to {maximum}, or Q to quit.")


def play_game():
    """Run one game session."""
    board, solution = make_puzzle()
    original_board = [row[:] for row in board]

    print("\nWelcome to Terminal Sudoku!")
    print("Fill the empty cells (shown as .) with numbers 1-9.")
    print("Enter row, column, and number when prompted. Type Q at any prompt to quit.")
    print("Enter 0 as the number to clear a cell you filled.\n")

    while True:
        print_board(board)

        if is_completed(board):
            if board == solution:
                print("Congratulations! You solved the Sudoku!")
            else:
                print("The board is full, but it is not correct yet. Keep checking your answers!")
            if board == solution:
                break

        row = get_integer("Row (1-9, or Q to quit): ", 1, 9)
        if row is None:
            break

        col = get_integer("Column (1-9, or Q to quit): ", 1, 9)
        if col is None:
            break

        number = get_integer("Number (1-9, 0 to clear, or Q to quit): ", 0, 9)
        if number is None:
            break

        row -= 1
        col -= 1

        if original_board[row][col] != EMPTY:
            print("That cell is part of the original puzzle and cannot be changed.")
            continue

        if number == EMPTY:
            board[row][col] = EMPTY
        elif number != solution[row][col]:
            print("That number is not correct for this puzzle. Try again.")
        else:
            board[row][col] = number

    print("\nThanks for playing Sudoku!")


def main():
    """Show the main menu and start the game."""
    while True:
        print("\n=== SUDOKU ===")
        print("1. New game")
        print("2. Rules")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("\nSudoku rules:")
            print("- Fill every row with numbers 1 through 9, without repeats.")
            print("- Fill every column with numbers 1 through 9, without repeats.")
            print("- Fill every 3x3 box with numbers 1 through 9, without repeats.")
            print("- Original puzzle numbers cannot be changed.")
            print("- Enter 0 to clear a cell you filled.")
            print("- Type Q at a prompt to quit the current game.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
