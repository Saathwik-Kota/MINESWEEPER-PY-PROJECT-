from board import Board,Box

def reveal_box(board,row,col):
    
    '''recursively reveals boxes starting from (row,col)
       
       it returns:
           'mine' if the box is a mine
           'ok' if the box has been revealed
           'invalid' if the move is invalid (if already revealed or flagged)'''
    
    
    if not (0 <= row <board.rows and 0 <= col < board.cols):
        return 'invalid'
    #checks if the row or col is out of bounds
    
    box = board.grid[row][col]
    
    if (box.is_revealed or box.is_flagged):
        return 'invalid'
    #cannot reveal a flagged or already revealed box
    
    box.is_revealed = True
    #reveals the box given it passes the above if statements
    
    if box.is_mine:
        return 'mine'
    #checks for game over
    
    if box.adjacent_mines == 0:
        for r,c in board.get_neighbors(row,col):
            if not board.grid[r][c].is_revealed:
                reveal_box(board,r,c) #recursive call
    #if adjacent mines is 0 , reveals neighbor boxes recursively
    
    return 'ok'

def toggle_flag(board,row,col):
    
    '''toggles a flag on the box (keeps a flag if there isn't one before
                                  or removes the flag is there is already one)
    
       it returns:
           'ok' if the flag is toggled
           'invalid' if the box is revealed'''
           
    
    if not(0 <= row < board.rows and 0 <= col < board.cols):
        return 'invalid'
    #checks if the row or col is out of bounds
    
    box = board.grid[row][col]
    
    if box.is_revealed:
        print("Cannot flag a revealed box")
        return 'invalid'
    #cannot toggle a revealed box
    
    box.is_flagged = not box.is_flagged
    #toggles the flag given the above if statements are passed
    
    return 'ok'

def check_win_condition(board):
    
    '''checks if the game is won
       win condition:
           all non-mine boxes should be revealed'''
           
    for r in range(board.rows):
        for c in range(board.cols):
            box = board.grid[r][c]
            if (not box.is_mine and not box.is_revealed):
                return False
            # if a box is not a mine and it isn't revealed, the game isn't over
    return True
    #if all non-mine boxes are revealed, the game has been won

       
