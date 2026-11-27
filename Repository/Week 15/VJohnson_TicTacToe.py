# Basically what we want to do is have the player input a number from 1 to 9, and then check if that space is available, and then write the players symbol to that space.
# After each turn, we display the board, and check for winning combination

# we use regex for input matching because we want to utilize case-insensitive matching.
import re

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
            #[[str(n) for _ in range(self.cols)] for _ in range(self.rows)]
            # This doesnt work because it is iterating through and changing each cell to 1, then each cell to 2, and so on. 
            for row in range(self.rows):
                for col in range(self.cols):
                    # Input is in string, so we're going to make the entries in the grid strings. 
                    # We can use isdigit() on a string, but cant on an integer
                    # there is likely a better way to do this, but this works and its only 9 operations. 
                    self.board[row][col] = str(n)
                    n = n + 1
            
    def displayBoard(self):
        # iterate through the current rows and print the values
        # Put the board in a nice little box
        # I prefer to use box drawing characters
        # https://en.wikipedia.org/wiki/Box-drawing_characters
        # Resisting the urge to transpose my powershell program that builds boxes, we're just going to do this one manually.
        # ┌───────────────────────┐
        # |     ┏━━━┳━━━┳━━━┓     |
        # |     ┃ 1 ┃ 2 ┃ 3 ┃     | 
        # |     ┣━━━╋━━━╋━━━┫     |
        # |     ┃ 4 ┃ 5 ┃ 6 ┃     | 
        # |     ┣━━━╋━━━╋━━━┫     |
        # |     ┃ 7 ┃ 8 ┃ 9 ┃     | 
        # |     ┗━━━┻━━━┻━━━┛     |
        # └───────────────────────┘
        print("┌───────────────────────┐")
        print("│     ┏━━━┳━━━┳━━━┓     │")
        for row in range(self.rows):
            print("│     ┃",self.board[row][0],"┃", self.board[row][1], "┃",self.board[row][2],"┃     │")
            if row != 2:
                # Print a pretty divider between the first and second rows
                print("│     ┣━━━╋━━━╋━━━┫     │")
        print("│     ┗━━━┻━━━┻━━━┛     │")
        print("└───────────────────────┘")

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
            "8" : (2,1),
            "9" : (2,2),
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
        if re.match(r"x",self.playerSelectionInput(),re.IGNORECASE):
            self.players["Player1"] = "X"
            self.players["Player2"] = "O"
        else:
            self.players["Player1"] = "O"
            self.players["Player2"] = "X"
        # We can now access the players symbols with self.players[player] where player equals "Player1" or "Player2"

    def isaValid(self,value):
        # Helper function to verify players input for selecting symbol.
        # They can only enter a symbol and we should not terminate the script if they mistakenly enter something else
        res = re.match(r"x|o",value,re.IGNORECASE)
        if res:
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

    def iscValid(self,value):
        # Helper function to verify if players would like to play again
        res = re.match("yes",value,re.IGNORECASE)
        if res:
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

    def playAgainInput(self):
        # Input loop, checks if the input is valid and prevents the script from breaking on invalid inputs.
        while True:
            confirm = self.iscValid(str(input("Play again? >")))
            if confirm is not None:
                return confirm
            else: 
                print('You must enter some variation of yes')

    def checkBoard(self):
        # Checks the combinations of coordinates to see if they're all the same symbol. 
        # If a winner is found, the winning player will be returned, otherwise, nothing will be returned
        # Define the Winning Combinations
        WinningCombinations = [
            # What this is actually doing is sectioning the board into discrete lists of rows, columns and diags, querying the actual board for its contents. 
            # This is why we do this when we check for winners, we want to overwrite this list with the current configuration every time we check. 
            # Rows
            [self.board.board[0][0],self.board.board[0][1],self.board.board[0][2]],
            [self.board.board[1][0],self.board.board[1][1],self.board.board[1][2]],
            [self.board.board[2][0],self.board.board[2][1],self.board.board[2][2]],
            # Columns
            [self.board.board[0][0],self.board.board[1][0],self.board.board[2][0]],
            [self.board.board[0][1],self.board.board[1][1],self.board.board[2][1]],
            [self.board.board[0][2],self.board.board[1][2],self.board.board[2][2]],
            # Diagonals
            [self.board.board[0][0],self.board.board[1][1],self.board.board[2][2]],
            [self.board.board[0][2],self.board.board[1][1],self.board.board[2][0]]
        ]
        # A combination is a list of 3 symbols as they appear on the board
        # Current player symbols are found in self.players
        # If the returned symbol is sym1, its player 1s victory. This means player 1 can be either X or O.
        syms = [self.players["Player1"],self.players["Player2"]]
        for combination in WinningCombinations:
            # Each element in WinningCombinations is a list, so we need to do this for each one
            # List Comprehension: Iterates through each element in each combination list, returning true if equal to syms[0], then all function returns true if all elements in the list are true.
            if all(ele == syms[0] for ele in combination) is True:
                return "p1"
            elif all(ele == syms[1] for ele in combination) is True:
                return "p2"

    def playerMove(self,sym):
        # Print the current board at the start of the turn
        self.board.displayBoard()
        # cell is a tuple containing 2 numbers, the x and y coordinate of the corresponding matrix
        cell = self.board.mapped.get(self.playerTurnInput())
        # Check the board, if it's a digit then it has not been played yet
        if self.board.board[cell[0]][cell[1]].isdigit() is False:
            # This space has been changed to a player symbol, and is inaccessible
            print("You must select an empty space (Numbered)")
            # Re-print the board
            self.board.displayBoard()
        else:
            # change the referenced cell in the matrix to the players symbol
            # We change the cell in the board with the active player symbol 
            self.board.board[cell[0]][cell[1]] = sym

    def splashScreen(self):
        # Display a welcome message, the rules, and prompt to continue before starting the game
        print("| ---      Welcome to Tic-Tac-Toe!   --- |")
        print("| ---                                --- |")
        print("| ---        By Vanessa Johnson      --- |")
        print("| ---             CS1101             --- |")
        print("| ---      The rules are simple:     --- |")
        print("| ---       Players take turns       --- |")
        print("| ---    choosing available spaces   --- |")
        print("| --- until either a winner is found --- |")
        print("| --- or all spaces have been filled --- |")
        print("| ---                                --- |")
        print("| ---  You may type quit at any time --- |")
        print("| ---       to exit the program      --- |")
        input("| ---      Press enter to begin!     --- |")

    def gameLoop(self):
        # The main game loop
        # Start on an odd turn (Player 1)
        turn = 1
        # While the game is active
        while turn <= 9:
            if turn % 2 == 0:
                # Player 2 turn
                print(f"Player 2 ({self.players["Player2"]}) turn")
                sym = self.players["Player2"]
            else:
                # Player 1 turn
                print(f"Player 1 ({self.players["Player1"]}) turn")
                sym = self.players["Player1"]
            self.playerMove(sym)
            # check the board for a winning configuration
            result = self.checkBoard()
            if result == "p1":
                # Checkboard returned a winner
                print(f"Winner is Player 1")
                self.board.displayBoard()
                self.playAgainInput()
            elif result == "p2":
                print(f"Winner is Player 2")
                self.board.displayBoard()
                self.playAgainInput()
            else:
                # No winner found, continue the game
                turn = turn + 1
        else:
            # 9 turns have commenced without a winner, the game is a draw
            self.board.displayBoard()
            print("No winner found!")
            self.playAgainInput()
        # Things that can end the game: Player types 'quit', turn is greater than 9, a winning combination is found. 
        # For quitting, we can look for quit in our isvalid functions 

def main():
    # create the board
    board = GameBoard()
    # create the game with the board
    game = TheGame(board)
    # play the game
    game.gameLoop()

main()