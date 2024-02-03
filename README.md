# [Tic-Tac-Toe](https://tic-tac-toe-svgint-bf602e1b6c57.herokuapp.com/)

Tic-Tac-Toe is a Python termonal game , which run in mock terminal in Heroku.
Two players are requred to play the game, The winner is the first player to put three of thier symbols in the row, column or dioganal. If non of the player achieve it its a draw.

[Click here or on the title of README.md to access live version of my project](https://tic-tac-toe-svgint-bf602e1b6c57.herokuapp.com/)

![Different screen devices with Tic-Tac-Toe](gallery/responsive.png)

## How to play

1. Game is played on a 3x3 board
2. Players choose the X or O for their symbol.
3. Players take turns to choose the cell on the game board.
4. Place three of the symbols in a row, column or dioganal and win
5. If the entire board is filled and there is no winner, the game is a draw. <br>
    Good Luck! :)

## Features

### Existing Features
 - Displays the set of rules of the game
 - Lets 1st player to choose X or O and assignes the other symbol to 2nd player
 ![Choosing player symbole](gallery/choosing_symbol.png)
 - Prints the tic tac toe game grid
 - Lets player to choose the row and column on the grid and places the chosen symbol on the game grid
 ![Placing players symbole on the grid](gallery/placing_move.png)
 - Switched the players after every move
 ![switching players](gallery/switching_players.png)
 - Will check row, colums and diogonals for the winner and display the winner as soon as the criteria to become one is achieved

 ![win dioganal](gallery/winDioganal.png)
 ![win row](gallery/winRow.png)
 ![win column](gallery/playerwinscolumn.png)
 - If the board is full and there is no winner will disply a message "Its a tie"
 ![displaying tie meassage](gallery/tie.png)
 - Input validation
   - Error message will appear if player will try to choose something other then X or O for their symbol
   ![player symbol error message](gallery/invalidPlayerSymbol.png)
   - Error message appears if not a number entered when choosing row and column
   ![Invalid input when choosing move](gallery/Invalid_input.png)
   - Out of range massage appears if player enetered number greater then 2 when coosing row or column.
   ![out of range error message](gallery/out_of_range.png)
   - Will flag if the chosen space is olready occupied
   ![existing move](gallery/alreadyOccupied.png)

   