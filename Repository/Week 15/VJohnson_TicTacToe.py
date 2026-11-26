# Basically what we want to do is have the player input a number from 1 to 9, and then check if that space is available, and then write the players symbol to that space.
# After each turn, we display the board, and check for winning combination

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
        n = 1
        while n <= 9:
            for row in range(self.rows):
                for col in range(self.cols):
                    # Input is in string, so we're going to make the entries in the grid strings. 
                    # We can use isdigit() on a string, but cant on an integer
                    # there is likely a better way to do this, but this works and its only 9 operations. 
                    self.board[row][col] = str(n)
                    n = n + 1
            
    def displayBoard(self):
        # iterate through the current rows and print the values
        for row in range(self.rows):
            print(self.board[row][0],"|", self.board[row][1], "|",self.board[row][2])
            if row != 2:
                # Print a pretty divider between the first and second rows
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
        # make the board a part of the game
        self.board = board
        # Valid selections are the numbers 1-9 as strings. Iterate through the range, converting them to strings, appending them to the valid array
        self.validset = []
        for _ in range(1,10): self.validset.append(str(_))
        # Create Player 1 and Player 2
        self.players = {
            "Player1" : " ",
            "Player2" : " ",
        }
        # Ask Player 1 what Symbol they want, then give player 2 the other symbol.
        player1sel = self.playerSelectionInput()
        if player1sel == "X":
            self.players["Player1"] = "X"
            self.players["Player2"] = "O"
        else:
            self.players["Player1"] = "O"
            self.players["Player2"] = "X"
        print(f"{self.players}")
        # We can now access the players symbol with self.players[player] where player equals "Player1" or "Player2" depending on turn count. 
        # start at turn 1. Odd turns will be player1, even turns will be player 2. 


    def isaValid(self,value):
        # Helper function to verify players input for selecting symbol.
        # They can only enter a symbol and we should not terminate the script if they mistakenly enter something else
        if value == "X" or value == "O":
            return value
        else:
            return None

    def isbValid(self,value):
        # Helper function to verify players input for their turn.
        # They can only enter a digit and we should not terminate the script if they mistakenly enter something else
        if value in self.validset:
            return value
        else:
            return None

    def playerSelectionInput(self):
        # Input loop, checks if the input is valid and prevents the script from breaking on invalid inputs.
        while True:
            sym = self.isaValid(str(input("X or O >")))
            if sym is not None:
                return sym
            else:
                print('You must enter X or O')

    def playerTurnInput(self):
        # Input loop, checks if the input is valid and prevents the script from breaking on invalid inputs.
        while True:
            move = self.isbValid(str(input("Enter 1 through 9 >")))
            if move is not None:
                return move
            else: 
                print('You must enter a value between 1 and 9')

    def playerMove(self):
        # cell is a tuple containing 2 numbers, the x and y coordinate of the corresponding matrix
        self.board.displayBoard()
        cell = self.board.mapped.get(self.playerTurnInput())
        # Check the board, if it's a digit then it has not been played yet
        if self.board.board[cell[0]][cell[1]].isdigit() is False:
            # This space has been changed to a player symbol, and is inaccessible
            print("You must select an empty space (Numbered)")
            self.board.displayBoard()
        else:
            # change the referenced cell in the matrix to the players symbol
            # We change the cell in the board with the active player symbol (NEEDS CHANGED TO SYM VARIALBE ONCE WE GET THERE)
            self.board.board[cell[0]][cell[1]] = "X"
            self.board.displayBoard()

def main():
    # create the board
    board = GameBoard()
    # create the game with the board
    game = TheGame(board)
    # play the game
main()