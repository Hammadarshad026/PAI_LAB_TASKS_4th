def print_board(board):
    for row in board:
        print(" ".join(row))  # Show the board in a simple way
    print("\n" + "-" * (len(board) * 2))  # Print a line for separation

def is_safe(board, row, col, n):
    # Check the column (above rows)
    for i in range(row):
        if board[i][col] == "Q":
            return False
    # Check the left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == "Q":
            return False
    # Check the right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == "Q":
            return False
    return True

def solve(board, row, n):
    if row == n:  
        print_board(board)
        return
    
    for col in range(n): 
        if is_safe(board, row, col, n):  
            board[row][col] = "Q"  # Place queen
            solve(board, row + 1, n)  # Move to the next row
            board[row][col] = "."  # Backtrack)

def n_queens(n):
    board = [["."] * n for _ in range(n)]  
    solve(board, 0, n)


n_queens(4)
