from board import Board
import game_logic
import fileio


def get_user_input():
    """
    Gets and checks user input.
    Expected formats:
    'r <row> <col>' (reveal)
    'f <row> <col>' (flag)
    'save', 'load', 'quit', 'new'
    """
    while True:
        try:
            user_input = input("Enter action (r(reveal)/f(flag) row col, save, load, new, quit): ").lower().strip()
            parts = user_input.split()

            if parts[0] in ['r', 'f'] and len(parts) == 3:
                action = parts[0]
                row = int(parts[1])
                col = int(parts[2])
                return [action, row, col]

            elif parts[0] in ['save', 'load', 'quit', 'new'] and len(parts) == 1:
                return parts[0], None, None

            else:
                print("Invalid input. Try again.")

        except ValueError:
            print("Invalid row/col. Please enter numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main_game_loop():
    """The main loop for the Minesweeper game."""
    board = None
    game_state = 'playing' # 'playing', 'won', 'lost'

    print("----------------WELCOME TO MINESWEEPER----------------")
    print("Type 'new' to start a new game or 'load' to load a saved game.")

    while True:
        if board:
            game_over_flag = (game_state in ['won', 'lost'])
            display = board.get_display_board(game_over=game_over_flag)
            print(display)

        if game_state == 'won':
            print("Congratulations! You've cleared all the mines!")
            game_state = 'playing' # Reset for new game
            board = None # Clear board
        elif game_state == 'lost':
            print("BOOM! You hit a mine. Game over.")
            game_state = 'playing' # Reset for new game
            board = None # Clear board

        [action, row, col] = get_user_input()

        if action == 'quit':
            print("----------------THANK YOU FOR PLAYING----------------")
            break

        if action == 'new':
            board = Board(rows=9, cols=9, no_mines=10)
            game_state = 'playing'
            print("Starting new game")
            continue
        if action == 'load':
            loaded_board = fileio.load_game()
            if loaded_board:
                board = loaded_board
                game_state = 'playing'
            continue

        if action == 'save':
            if board:
                fileio.save_game(board)
            else:
                print("No game in progress to save.")
            continue

        # --- Gameplay Actions ---
        if not board:
            print("Please start a 'new' game or 'load' a game first.")
            continue

        if not board.mines_placed:  
            board.place_mines()

        if game_state == 'playing':
            if action == 'r':
                result = game_logic.reveal_box(board, row, col)
                if result == 'mine':
                    game_state = 'lost'

            elif action == 'f':
                game_logic.toggle_flag(board, row, col)

            # Check for win condition after a valid reveal
            if action == 'r' and game_state == 'playing':
                if game_logic.check_win_condition(board):
                    game_state = 'won'

if __name__ == "__main__":
    main_game_loop()
