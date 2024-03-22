# Tic-Tac-Toe Board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the Tic-Tac-Toe board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if the current player has won
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (a draw)
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to evaluate the current state of the board
def evaluate_board():
    if check_winner('X'):
        return -1  # Human wins
    elif check_winner('O'):
        return 1   # AI wins
    elif is_board_full():
        return 0   # Draw
    else:
        return None  # Game is still ongoing

# Minimax function with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    score = evaluate_board()

    if score is not None:
        return score

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval_score = minimax(depth + 1, False, alpha, beta)
                    board[i][j] = ' '

                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)

                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval_score = minimax(depth + 1, True, alpha, beta)
                    board[i][j] = ' '

                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)

                    if beta <= alpha:
                        break
        return min_eval

# Function to make the AI move using the minimax algorithm
def ai_move():
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(0, False, float('-inf'), float('inf'))
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    board[best_move[0]][best_move[1]] = 'O'

# Main game loop
while True:
    display_board()

    # Human move
    row = int(input("Enter the row (0, 1, or 2): "))
    col = int(input("Enter the column (0, 1, or 2): "))
    if board[row][col] == ' ':
        board[row][col] = 'X'
    else:
        print("Invalid move. Cell already occupied.")
        continue

    # Check game state
    game_result = evaluate_board()
    if game_result is not None:
        display_board()
        if game_result == -1:
            print("You win!")
        elif game_result == 1:
            print("AI wins!")
        else:
            print("It's a draw!")
        break

    # AI move
    ai_move()

    # Check game state
    game_result = evaluate_board()
    if game_result is not None:
        display_board()
        if game_result == -1:
            print("You win!")
        elif game_result == 1:
            print("AI wins!")
        else:
            print("It's a draw!")
        break

