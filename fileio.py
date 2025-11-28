import os
import json
from board import Board

save_file = "minesweeper_save.txt"

def save_game(board):
    #This function saves the current board state to a file.
    game_state = {'board': board.to_dict()}
    try:
        with open(save_file,"w") as f:
            json.dump(game_state,f,i=4)
        print(f"Game is saved to {save_file}")
    except Exception:
        print("Error in saving the game")

def load_game():
    #This function loads a game state from a file.
    #It returns the board if load is successful and none if there is an error   
    if not os.path.exists(save_file):
        print("No save file found")
        return None
    try:
        with open(save_file,"r") as f:
            game_state = json.load(f)
            board = Board.from_dict(game_state['board'])
            print(f"Game is loaded from {save_file}")
            return board
    except Exception:
        print("An Error has occured. Starting new game...")
        return None
