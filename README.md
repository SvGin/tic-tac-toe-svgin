# [Tic-Tac-Toe](https://tic-tac-toe-svgint-bf602e1b6c57.herokuapp.com/)

Tic-Tac-Toe is a Python terminal game, which runs in mock terminal in Heroku.
Two players are required to play the game, the winner is the first player to put three of thier symbols in a row, column or diagonal. If none of the players achieve it, it's a draw.

[Click here or on the title of README.md to access live version of my project](https://tic-tac-toe-svgint-bf602e1b6c57.herokuapp.com/)

![Different screen devices with Tic-Tac-Toe](gallery/responsive.png)

## How to play

1. The game is played on a 3x3 board
2. Players choose the X or O for their symbol.
3. Players take turns to choose the cell on the game board.
4. Place three of the symbols in a row, column or diagonal to win
5. If the entire board is filled and there is no winner, the game is a draw. <br>
    Good Luck! :)

## Features

### Existing Features
 - Displays the set of rules of the game
 - Lets the 1st player choose X or O and assigns the other symbol to the 2nd player
 ![Choosing player symbol](gallery/choosing_symbol.png)
 - Prints the tic tac toe game grid
 - Lets the player choose the row and column on the grid and places the chosen symbol on the game grid
 ![Placing players symbol on the grid](gallery/placing_move.png)
 - Switch the players after every move
 ![switching players](gallery/switching_players.png)
 - Will check row, columns and diagonals for the winner and display who the winner is as soon as the criteria is met

 ![win dioganal](gallery/winDioganal.png)
 ![win row](gallery/winRow.png)
 ![win column](gallery/playerwinscolumn.png)
 - If the board is full and there is no winner, there will be a display message of "Its a tie" <br>
 ![displaying tie meassage](gallery/tie.png)
 - Input validation
   - Error message will appear if player will tries to choose something other then X or O for their symbol
   ![player symbol error message](gallery/invalidPlayerSymbol.png)
   - Error message appears if it's not a number entered when choosing a row or column
   ![Invalid input when choosing move](gallery/Invalid_input.png)
   - Out of range message appears if player enetered a number greater then 2 when choosing a row or column.
   ![out of range error message](gallery/out_of_range.png)
   - Will flag if the chosen space is already occupied
   ![existing move](gallery/alreadyOccupied.png)

## Future Features

Create a game to play against a computer and to be able to switch between playing against the computer and 2 player mode

## Bugs

Solved bugs:

 - Had few issues with indentations and was not able to run the code.

 - Had a mistake in def move function which made my code run in the loop without moving to the nextstep in the game, took me a while to spot it.
 
## Validator Testing
Checked in PEP8
 - No Errors
![PEP8](gallery/validator.png)

## Deployment
To deploy this project I followed step by step instructions from Code Institute Deployment Video
 - In Heroku I opened the dashboard
 - Created a new app 
 - Conected my GitHub and chose the needed repo
 - In settings I did Reveal Config Vars PORT 8000
 - Add buildpacks: 1.python and 2.nodejs
 - Chose manual deploymnet and deployed Branch
 - View App

## Credits
 - https://github.com/SvGin/tic_tac_toe/blob/main/run.py This is my repo in GitHub. When I started my 3rd project I used the wrong template and when I did a Deployment I realised my mistake. So I created a new repo using the correct template and most of the code comes from my first attempt :)
  - For inspiration and some guidance I used the resources below:
    - [GitHub](https://gist.github.com/qianguigui1104/edb3b11b33c78e5894aad7908c773353)
    - [tic-tac-toe-game-in-python](https://www.c-sharpcorner.com/UploadFile/75a48f/tic-tac-toe-game-in-python/)
    - [CodeInstitute ReadME](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
    - Love Sandwiches - Essentials Project from Code Institute
     - [How to code tic tac toe in python](https://www.youtube.com/watch?v=n2o8ckO-lfk)
     - [Python TIC TAC TOE Tutorial](https://www.youtube.com/watch?v=dK6gJw4-NCo&list=PLr66KBzyOhBXULXhbdP_Z5dGmSiI27fVc)
