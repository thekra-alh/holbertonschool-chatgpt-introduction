#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Validate input
        try:
            row = int(input(f"Enter row (0,1,2) for player {player}: "))
            col = int(input(f"Enter column (0,1,2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")
            continue

        # Check bounds
        if row not in range(3) or col not in range(3):
            print("Row and column must be 0, 1, or 2.\n")
            continue

        # Check if cell is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        # Place mark
        board[row][col] = player

        # Check winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
