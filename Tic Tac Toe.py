import random

board = ['-'] * 9
player_symbol='X'
ai_symbol='O'

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print("-------------")

# Function to check if a player has won
def check_winner(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

# Function for the AI to make a move based on predefined strategies
def ai_make_move(board):
    # Predefined strategies for the AI
    possible_moves = [
        [4],            # Center move if available
        [0, 2, 6, 8],   # Corner moves
        [1, 3, 5, 7]    # Side moves
    ]

    # Try each strategy in order
    for moves in possible_moves:
        available_moves = [move for move in moves if board[move] == '-']
        if available_moves:
            return random.choice(available_moves)

    # If no predefined moves are possible (should not happen in a standard game)
    return random.choice([i for i in range(9) if board[i] == '-'])

# Game loop
while True:
    print_board(board)

    # Player's turn
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == '-':
        board[player_move] = player_symbol
        if check_winner(board, player_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif '-' not in board:
            print_board(board)
            print("It's a tie!")
            break

        # AI's turn
        ai_move = ai_make_move(board)
        board[ai_move] = ai_symbol
        if check_winner(board, ai_symbol):
            print_board(board)
            print("The AI wins! Better luck next time.")
            break
        elif '-' not in board:
            print_board(board)
            print("It's a tie!")
            break
    else:
        print("That cell is already taken. Please try again.")