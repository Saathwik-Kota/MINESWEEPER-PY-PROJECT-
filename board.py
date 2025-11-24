import random

class Box:
    
    # Represents a single box on the board.
    
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

    def to_dict(self):

        # For converting box state to dict to save in file.
        # returns a dictionary
        return {
            'is_mine': self.is_mine,
            'is_revealed': self.is_revealed,
            'is_flagged': self.is_flagged,
            'adjacent_mines': self.adjacent_mines
        }

  
    @classmethod
    def from_dict(cls, data):
        # For converting dict from file to box state

        box = cls() 
        box.is_mine = data['is_mine']
        box.is_revealed = data['is_revealed']
        box.is_flagged = data['is_flagged']
        box.adjacent_mines = data['adjacent_mines']
        return box

class Board:
    
    def __init__(self, rows=9, cols=9, no_mines=10):
        self.rows = rows
        self.cols = cols
        self.no_mines = no_mines

        # Board consisting of 81 boxes
        self.grid = [[Box() for i in range(cols)] for j in range(rows)]

        self.mines_placed = False

    

    def place_mines(self):

        """
        Used random beacuse if we dont use random the mine placement 
        will be same for every game.
        """
        mines_to_place = self.no_mines
        
        while mines_to_place > 0:

          # randint is different from range it includes self.rows-1 and self.cols-1

            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            
          
            if not self.grid[row][col].is_mine:
                self.grid[row][col].is_mine = True
                mines_to_place -= 1
        
        self.mines_placed = True

        # To know adjacent mines to non_mines
        self.calculate_adjacent_mines()

    def calculate_adjacent_mines(self):
        
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.grid[i][j].is_mine:
                    count = 0
                    for dr, dc in self.get_neighbors(i, j):
                        if self.grid[dr][dc].is_mine:
                            count += 1
                    self.grid[i][j].adjacent_mines = count

    def get_neighbors(self, row, col):

      # Returns a list of neighbour coordinates

        neighbours = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # To make sure this works no matter the position of the box
                if (i, j) != (row, col) and (0 <= i < self.rows) and (0 <= j < self.cols):
                    neighbours.append((i, j))
        return neighbours

    def get_display_board(self, game_over=False):
        """
        Displays one of these depending on the box state:
        - '?' for hidden
        - 'F' for flagged
        - '*' for mine (if game over)
        - ' ' for 0 adjacent mines (if revealed)
        - Number for adjacent mines (if revealed)
        - 'X' for a mine you clicked on
        """
        display = []
        # Proper structure for the board
        col_indexing = "   " + " ".join([str(i) for i in range(self.cols)])
        display.append(col_indexing)
        display.append("  " + "-" * (self.cols * 2 - 1))

        for i in range(self.rows):
            row_str = f"{i:2}|" # Indexing for rows
            for j in range(self.cols):
                box = self.grid[i][j]
                if game_over and box.is_mine and not box.is_revealed:
                    row_str += "* " # Show all mines on game over
                elif box.is_revealed:
                    if box.is_mine:
                        row_str += "X " # The mine that was clicked
                    elif box.adjacent_mines > 0:
                        row_str += f"{box.adjacent_mines} "
                    else:
                        row_str += "  " # Empty, revealed cell
                elif box.is_flagged:
                    row_str += "F "
                else:
                    row_str += "? "
            display.append(row_str)
        return "\n".join(display) # Final display of all rows

    def to_dict(self):
        # To covert into dictionary
        return {
            'rows': self.rows,
            'cols': self.cols,
            'no_mines': self.no_mines,
            'mines_placed': self.mines_placed,
            'grid': [[box.to_dict() for box in row] for row in self.grid]
        }

    @classmethod
    def from_dict(cls, data):
        # To covert dictionary to object
        board = cls(data['rows'], data['cols'], data['no_mines'])
        board.mines_placed = data['mines_placed']
        board.grid = [[Box.from_dict(box_data) for box_data in row] for row in data['grid']]
        return board