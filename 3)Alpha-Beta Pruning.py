import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        print(board[3*i], '|', board[3*i+1], '|', board[3*i+2])
        if i < 2:
            print('---------')

# Check for winner
def check_winner(brd, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in win_combinations:
        if all(brd[pos] == player for pos in combo):
            return True
    return False

# Check if board is full
def is_full(brd):
    return ' ' not in brd

# Evaluate board (heuristic)
def evaluate(brd):
    if check_winner(brd, 'X'):
        return 10
    elif check_winner(brd, 'O'):
        return -10
    else:
        return 0

# Minimax with Alpha-Beta Pruning
def minimax(brd, depth, is_maximizing, alpha, beta):
    score = evaluate(brd)
    if score == 10 or score == -10:
        return score
    if is_full(brd):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                val = minimax(brd, depth + 1, False, alpha, beta)
                brd[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                val = minimax(brd, depth + 1, True, alpha, beta)
                brd[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

# Find best move
def find_best_move():
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# Game loop
def play_game():
    print("Tic-Tac-Toe using Minimax with Alpha-Beta Pruning")
    print_board()

    while True:
        player_move = int(input("\nEnter your move (1-9): ")) - 1
        if board[player_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[player_move] = 'O'

        if check_winner(board, 'O'):
            print_board()
            print("You win!")
            break

        if is_full(board):
            print_board()
            print("It's a draw!")
            break

        ai_move = find_best_move()
        board[ai_move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()
