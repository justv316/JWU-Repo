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
                    self.board[row][col] = str(n)
                    n = n + 1
            
    def displayBoard(self):
        # iterate through the current rows and print the values
        for row in range(self.rows):
            print(self.board[row][0],"|", self.board[row][1], "|",self.board[row][2])
            if row != 2:
                print("--+---+--")

    def mapBoard(self):
        # Players will call the numbered cell which correlates to a location in the matrix.
        # Will modify value in self.board[x][y]
        self.mapped = {
            "1" : (0,0),
            "2" : (0,1),
            "3" : (0,2),
            "4" : (1,0),
            "5" : (1,1),
            "6" : (1,2),
            "7" : (2,0),
            "8" : (0,1),
            "9" : (0,2),
        }

class TheGame():
    def __init__(self,board):
        self.valid = []
        # Valid selections are the numbers 1-9 as strings. Iterate through the range, converting them to strings, and appending them to the valid array
        for _ in range(1,10): self.valid.append(str(_))
        self.board = board
    def isValid(value,valid):
        # Helper function to verify players input.
        # They can only enter a digit and we should not terminate the script if they mistakenly enter something else
        # We must also loop the input request when the player enters a cell that's already been written to.
        # Lets instead create this as part of the game class, so we only do it once.
        if value in valid:
            return value
        else:
            return None

    def playerInput(self):
        while True:
            move = self.isValid(str(input("Enter 1 through 9 >")))
            if move is not None:
                return move
            else: 
                print('You must enter a value between 1 and 9')

    def playerMove(board):
        # cell is a tuple containing 2 numbers, the x and y coordinate of the corresponding matrix
        cell = board.mapped.get(self.playerInput())
        # Check the board, if it's a digit then it has not been played yet
        if board.board[cell[0]][cell[1]].isdigit() is False:
            # This space has been changed to a player symbol, and is inaccessible
            print("You must select an empty space (Numbered)")
        else:
            # change the referenced cell in the matrix to the players symbol
            # We change the cell in the board with the active player symbol (NEEDS CHANGED TO SYM VARIALBE ONCE WE GET THERE)
            board.board[cell[0]][cell[1]] = "X"


def main():
    board = GameBoard()
    game = TheGame(board)
    game.playerMove()
main()
    # create the game
    # feed the game into the board
    # run the main loop