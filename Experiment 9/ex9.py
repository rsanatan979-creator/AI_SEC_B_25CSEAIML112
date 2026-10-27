def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

for turn in range(9):
    print("\nCurrent board:")
    print_board(board)

    print(f"Player {player}'s turn")

    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position! Enter numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That position is already occupied! Try again.")
            continue

    except ValueError:
        print("Please enter numbers only.")
        continue

    board[row][col] = player

    if check_winner(board):
        print("\nFinal board:")
        print_board(board)
        print(f"Player {player} wins!")
        break

    player = "O" if player == "X" else "X"

else:
    print("\nFinal board:")
    print_board(board)
    print("Game Draw!")