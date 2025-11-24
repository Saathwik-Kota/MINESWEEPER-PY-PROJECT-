import os
import json
from board import Board

SAVE_FILE = "minesweeper_save.txt"

def save_game(board):
    
    """This function saves the current board state to a file.
    We use JSON for this."""
    
    game_state = {'board': board.to_dict()}

    try:
        with open(SAVE_FILE,"w") as file:
            json.dump(game_state, file, indent=4)
        print(f"Game saved to {SAVE_FILE}")
    except IOError as e:
        print(f"Error saving game: {e}")

def load_game():
    
    """This function loads a game state from a file.
    It returns: 1)"Board" if "load" is successful.
                  2)"None" if "file not found" or "error"."""
        
    if not os.path.exists(SAVE_FILE):
        print("No save file found")
        return None

    try:
        with open(SAVE_FILE,"r") as file:
            game_state = json.load(file)

            board = Board.from_dict(game_state['board'])

            print(f"Game loaded from {SAVE_FILE}")
            return board

    except IOError as e:
        print(f"IO error occurred: {e}. Starting new game.")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}. Starting new game.")
        return None
    except KeyError as e:
        print(f"Missing key error: {e}. Starting new game.")
        return None