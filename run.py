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



def play_game():
    """
    This function contains all other needed functions to start and play the game
    """
    introduction()


#Call main funcion, start the game
play_game()
