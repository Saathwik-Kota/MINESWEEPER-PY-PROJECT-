-------------------------------------------------------------------------------------------MINESWEEPER CONSOLE GAME--------------------------------------------------------------------------------------------------

-> This is a console based implementation of the classic minesweeper game.

1] PROJECT FEATURES :

Classic Gameplay       : Implement standard Minesweeper rules.
Reveal and Flag        : Allows players to reveal boxes or place/remove flags.
Recursive Reveal       : Automatically reveals adjacent empty cells upon clicking a cell with zero surrounding mines.
Game State Persistence : Ability to **save** and **load** the current game state using JSON file I/O.
Dynamic Board Display  : A clean, indexed console display that updates after every move.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2] DIRECTORY STRUCTURE :

-> The project is organized into modular files :

board.py             : Defines the Box and Board classes, handling board initialization and mine placement. 
game_logic.py        : Contains core game logic like revealing a box, toggling a flag, and checking win condition. 
fileio.py            : Handles saving and loading the game state to/from a file.
main.py              : The main execution file containing the game loop and user input handling.
README.md            : This file.  
minesweeper_save.txt : The file where the game state is saved (created upon first save).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3] GAME INSTRUCTIONS :

# Goal

-> The objective is to reveal all the boxes that DO NOT contain a mine.

* When you reveal a box, a number appears, indicating how many mines are adjacent to that box (horizontally, vertically, and diagonally).
* If you reveal a mine, the game is over.
* You can use a **flag** to mark boxes you suspect contain a mine.

# Console Commands

-> The game requires the user to input a command, followed by row and column coordinates (0-indexed).

  ACTION      |  Format        | Example | Description                           |
 ---------------------------------------------------------------------------------      
 **Reveal**   |  r <row> <col> |  r 4 5  | Reveals the box at (row, col).        |
 **Flag**     |  f <row> <col> |  f 2 8  | Toggles a flag on/off at (row, col).  |
 **Save**     |  save          |  save   | Saves the current game state.         |
 **Load**     |  load          |  load   | Loads the last saved game state.      |
 **New Game** |  new           |  new    | Starts a new 9x9 board with 10 mines. |
 **Quit**     |  quit          |  quit   | Exits the game.                       |

# Board Symbols

| Symbol  | Description                                  |
----------------------------------------------------------
|  ?      | Hidden (unrevealed and unflagged) box.       | 
|  F      | Flagged box.                                 |
|  1-8    | Revealed box with $N$ adjacent mines.        |
| (space) | Revealed box with 0 adjacent mines.          |
|  X      | The mine you clicked on (Game Over).         |
|  *      | Unclicked mines (shown only when Game Over). |

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4] SETUP AND RUNNING :

# Prerequisites

-> Python Compiler.

# Installation

-> No special installation is required beyond having Python installed. Simply clone the repository or place all the (.py) files in the same directory.

# How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the main script :
  ->python3 main.py
3.  Follow the prompts to start a **new** game or **load** a previous one.

-------------------------------------------------------------------------------------------------THANK YOU-----------------------------------------------------------------------------------------------------------

