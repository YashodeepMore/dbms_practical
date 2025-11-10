# N-Queens Problem using Backtracking and Branch & Bound

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

# ---------------- BACKTRACKING ALGORITHM ----------------
def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_backtracking(board, row, n):
    if row == n:
        print_board(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_backtracking(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False

def n_queens_backtracking(n):
    print("\n--- Solving using Backtracking ---")
    board = [[0]*n for _ in range(n)]
    if not solve_backtracking(board, 0, n):
        print("No solution found.")


# ---------------- BRANCH AND BOUND ALGORITHM ----------------
def solve_branch_bound(row, n, board, col_used, d1, d2):
    if row == n:
        print_board(board)
        return True
    for col in range(n):
        if not col_used[col] and not d1[row - col + n - 1] and not d2[row + col]:
            board[row][col] = 1
            col_used[col] = d1[row - col + n - 1] = d2[row + col] = True
            if solve_branch_bound(row + 1, n, board, col_used, d1, d2):
                return True
            # Backtrack
            board[row][col] = 0
            col_used[col] = d1[row - col + n - 1] = d2[row + col] = False
    return False

def n_queens_branch_bound(n):
    print("\n--- Solving using Branch and Bound ---")
    board = [[0]*n for _ in range(n)]
    col_used = [False]*n
    d1 = [False]*(2*n - 1)  # Left diagonals
    d2 = [False]*(2*n - 1)  # Right diagonals
    if not solve_branch_bound(0, n, board, col_used, d1, d2):
        print("No solution found.")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    n_queens_backtracking(n)
    n_queens_branch_bound(n)
