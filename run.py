def introduction():
    """
    This function contains greating and rules of the game
    """
    print("Welcome to the game Tic-Tac-Toe!\n")
    print("Please read rules of the game: \n")
    print("1. Game is played on a 3x3 board")
    print("2. Players choose the X or O for their symbol")
    print("3. Players take turns to choose the cell on the game board")
    print("4. Place three of the symbols in a row, column or diagonals and win")
    print("5. If the entire board is filled, the game is a draw.\n")
    print("Good Luck! :)\n")


def player_symbols():
    """
    Player 1 will choose the symbol form X or O
    Will return error message is other symbole is selected
    """
    player1 = input("Please Choose X or O: \n").upper()
    while player1 not in ["X", "O"]:
        print("Invalid input, please choose from X , O\n")
        player1 = input("Please Choose X or O: \n").upper()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return player1, player2


def print_board(board):
    """
    Creating and printing game board
    Limits how many rows are printed out
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 10)


def out_of_board(row, col):
    """
    To check if chosen row and column are valid and not out of boards range
    """
    return 0 <= row <= 2 and 0 <= col <= 2


def player_move(player):
    """
    Player to imput row and column for the move
    Check if the move seleceted by the player is inside the board
    Check if number entered and not a letter or other symbol
    To display the error message if needed criteria is not met
    """
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2)\n"))
            col = int(input(f"Player {player}, enter column (0, 1, or 2)\n"))

            if out_of_board(row, col):
                return row, col
            else:
                print("Out of range. Please choose beween 0 and 2\n")
        except ValueError:
            print("Invalid input. Please enter 0, 1 or 2. Please try again!\n")


def move(board, player, row, col):
    """
    To recognise players move
    To let player know if the cell is alredy occupied
    and if so ask to enter row and column again
    """
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("Please try again. This cell is already occupied \n")
        new_row, new_col = player_move(player)
        move(board, player, new_row, new_col)


def player_swap(current_player, player_first, player_second):
    """
    Players to take turns after move registerd on the board
    """
    return player_second if current_player == player_first else player_first


def full_board(board):
    """
    Check of the bard is full
    """
    for row in board:
        if " " in row:
            return False
        return True


def if_winner(board):
    """
    Checking rows, colums and diagonals for the winner
    """
    # Will heck rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Will check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Will check both diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None


def play_game():
    """
    This function contains all other needed functions
    to start and play the game
    """
    introduction()
    player1, player2 = player_symbols()
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = player1

    while True:
        print_board(board)
        row, col = player_move(current_player)
        move(board, current_player, row, col)
        winner = if_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")

            break

        if full_board(board):
            print_board(board)
            print("Its a tie!")

            break
        current_player = player_swap(current_player, player1, player2)


play_game()
