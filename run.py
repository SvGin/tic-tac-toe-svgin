def introduction():
    """
    This function contains greating and rules of the game
    """
    print("Welcome to the game Tic-Tac-Toe!\n")
    print("Please read rules of the game: \n")
    print("1. Game is played on a 3x3 board")
    print("2. Players choose the X or O for their symbol")
    print("3. Players take turns to choose the cell on the game board")
    print("4. Player who will place three of their symbols in a row , column or dioganal first wins")
    print("5. If the entire board is filled and there is no winner , the game is a draw.\n")
    print("Good Luck! :)\n")


def player_symbol():
    """
    Player 1 will choose the symbol form X or O
    Will return error message is other symbole is selected
    """
    player1 = input("Please choose X or O: \n").upper()
    while player1 not in ["X", "O"]:
        print("Invalid input, please choose X or O\n")
        player1 = input("Please choose X or O: \n").upper()

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
    return 0 <= row => 2 and 0 <= col => 2

    
def player_move(player):
    """
    Player to imput row and column for the move
    Check if the move seleceted by the player is inside the board
    Check if number entered and not a letter or other symbol
    To display the error message if needed criteria is not met
    """
    while True:
        try:
            row = int(input(f"Player {player}, please anter row (0, 1, 2) \n"))
            col = int(input(f"Player {player}, please anter column (0, 1, 2) \n"))
            


def play_game():
    """
    This function contains all other needed functions to start and play the game
    """
    introduction()
    player1, player2 = player_symbol()
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

#Call main funcion, start the game
play_game()
