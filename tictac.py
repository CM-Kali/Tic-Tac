import numpy as np

# Create a 3x3 board filled with spaces
board = np.full((3, 3), ' ')

def display_board():
    print("\nCurrent Board:")
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            print(board[i][j] if board[i][j] != ' ' else str(i * 3 + j + 1), end="")
            if j < 2:
                print(" | ", end="")
        if i < 2:
            print("\n-----------", end="")
        print()
    print()

def check_win(player):
    # Check rows, columns and diagonals
    for i in range(3):
        if np.all(board[i, :] == player):  # Row
            return True
        if np.all(board[:, i] == player):  # Column
            return True
    if np.all(np.diag(board) == player):      # Main diagonal
        return True
    if np.all(np.diag(np.fliplr(board)) == player):  # Anti-diagonal
        return True
    return False

def is_draw():
    return np.all(board != ' ')

def reset_board():
    global board
    board = np.full((3, 3), ' ')

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != ' ':
                print("That cell is already taken. Choose another.")
                continue
            board[row][col] = player
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    print("Tic-Tac-Toe Game (2 Players)\n")
    print("Positions are numbered 1–9 as follows:")
    print(" 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n")

    player = 'X'
    while True:
        display_board()
        get_move(player)

        if check_win(player):
            display_board()
            print(f"🎉 Player {player} wins!\n")
            break
        elif is_draw():
            display_board()
            print("It's a draw!\n")
            break
        else:
            player = 'O' if player == 'X' else 'X'  # Switch player

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
    reset_board()
