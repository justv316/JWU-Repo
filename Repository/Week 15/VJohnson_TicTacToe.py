class GameBoard():
    def __init__(self):
        self.createBoard()
        self.mapBoard()

    def createBoard(self):
        self.rows, self.cols = 3, 3
        # iterates through each column and creates rows as independent objects
        # cells can be referenced by indexing board
        # example board[0][0] represents the cell in the top left, board[2][2] represents the cell in the bottom right.
        # This is list comprehension [expression for item in iterable] for item in iterable 
        self.board = [[str(" ") for _ in range(self.cols)] for _ in range(self.rows)]
        # Number each cell 1 through 9
        # I would really like to figure out how to do this in a one liner or something less expensive
        # Basically what we want to do is have the player input a number from 1 to 9, and then check if that space is available, and then write the players symbol to that space.
        # After each turn, we display the board, and check for winning combination
        n = 1
        while n <= 9:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.board[row][col] = n
                    n = n + 1
            
    def displayBoard(self):
        # iterate through the current rows and print the values
        for row in range(self.rows):
            print(self.board[row][0],"|", self.board[row][1], "|",self.board[row][2])
            if row != 2:
                print("--+---+--")

    def mapBoard(self):
        # Players will call the numbered cell which correlates to a location in the matrix.
        self.mapped = {
            "1" : self.board[0][0],
            "2" : self.board[0][1],
            "3" : self.board[0][2],
            "4" : self.board[1][0],
            "5" : self.board[1][1],
            "6" : self.board[1][2],
            "7" : self.board[2][0],
            "8" : self.board[2][1],
            "9" : self.board[2][2]
        }

    def playerMove(self):
        move = str(input(f"Enter 1 through 9 >"))
        if self.mapped.get(move).isdigit() is False:
            # This space has been changed to a player symbol, and is inaccessible
            print("You must select an empty space (Numbered)")
        else:
            self.mapped.get(move) = "X"


def main():
    board = GameBoard()
    #board.displayBoard()
    move = str(input(f"Enter 1 through 9 >"))
    print(board.mapped.get(move))
main()
    # create the game
    # feed the game into the board
    # run the main loop