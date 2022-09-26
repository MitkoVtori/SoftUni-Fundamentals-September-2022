def check_win(board, player):
    # check rows
    for rows in range(3):
        row = board[rows]
        if row.count(player) == 3:
            return True

    # check columns
    for columns in range(3):
        column = [row[columns] for row in board]
        if column.count(player) == 3:
            return True

    # check diagonals
    primary_diagonal = [board[diagonal][diagonal] for diagonal in range(3)]
    if primary_diagonal.count(player) == 3:
        return True

    secondary_diagonal = [board[secondary_diagonal][len(board) - secondary_diagonal - 1] for secondary_diagonal
                          in range(3)]
    if secondary_diagonal.count(player) == 3:
        return True

    return False


board = []
for winner in range(3):
    board.append(input().split())

if check_win(board, "1"):
    print("First player won")
elif check_win(board, "2"):
    print("Second player won")
else:
    print("Draw!")
