# we need random to generate a random number, assign it as r for ease of use
import random as r

def playerTurn():
    # Helper function for handling player input
    aInput = playerInput()
    if aInput == "Hit" or aInput == "hit":
        #return pScore + hitMe()
        return "hit"
    elif aInput == "Stand" or aInput == "stand":
        #return pScore
        return "stand"

def playerInput():
    # Helper function for capturing input
    while True:
        aInput = isaValid(input("| Hit or Stand |"))
        # Return valid input to the calling function
        if aInput is not None:
            return aInput
        # Ask again
        else:
            print("You must make a valid selection")

def isaValid(value):
    # Helper function for input validation
    # It may be more ideal to use regex to match valid terms because of pythons case sensitivity.
    validInput = ["Hit","Stand","hit","stand"]
    # Return the string if it's one of the expected terms
    if value in validInput:
        return value
    else:
        return None

def hitMe(value):
    # Helper function, adds a number between 2 and 11 to input
    return value + r.randrange(2,12)

def checkWinner(pScore,cScore):
    # Helper function to determine winner
    print(f"Player Hand: {pScore} Computer Hand: {cScore}")
    if pScore > 21:
        print("Computer Win! Player Loss!")
        return "computer"
    elif cScore > 21:
        print("Player Win! Computer Loss!")
        return "player"
    elif pScore > cScore:
        print("Player Win! Computer Loss!")
        return "player"
    elif pScore < cScore:
        print("Computer Win! Player Loss!")
        return "computer"
    elif pScore == cScore:
        print("It's a draw!")
        return None

def gameRound(gRound,pWins,pLoss):
    # score variables
    pScore = 0
    cScore = 0
    # initialize computer turn boolean as false so we can check for it
    cTurn = False
    # Start round
    print(f"| It is round {gRound} |")
    print(f"| Wins: {pWins} |")
    print(f"| Losses: {pLoss} |")
    pTurn = True
    # pScore starts at 0
    print(f"| Current hand value is {pScore} |")
    # We automatically hit for the player to begin the game proper
    pScore = hitMe(pScore)
    while pTurn == True:
        # check score if 21, busted, or fine to continue
        if pScore >= 21:
            if pScore == 21:
                # 21 is an auto-stand
                print("| You scored 21! |")
                # End Player Turn
                pTurn = False
                # Begin Computer Turn
                cTurn = True
                break
                # The instructions do not state that 21 is an auto-win for the player so we are not treating it as one
            elif pScore > 21:
                # Over 21 is an auto-loss
                print("| You have busted! |")
                # End Player Turn
                pTurn = False
                # Skip Computer Turn
                break
        else:
            print(f"| Current hand value is {pScore} |")
            # ask player to hit or stand
            aInput = playerTurn()
        if aInput == "hit":
            # produce a new score based on current score and check it for validity
            pScore = hitMe(pScore)
        elif aInput == "stand":
            # we only ever get here if the score is valid in the first place, so we do not need to call checkScore
            #pScore = checkScore(pScore)
            # begin Computer Turn
            cTurn = True
            # end Player Turn
            pTurn = False
        else:
            # Loop until we get an 'ending' result (bust, stand)
            print(f"| Current hand value is {pScore} |")
    # Computers turn
    while cTurn == True:
        # Score begins at 0
        print(f"| Computer score is {cScore} |")
        # Will perform hit me while the score is less than or equal to 16 and will stand if the score is over 16
        if cScore > 21:
            # over 21 is an auto-loss
            print("| The computer busted! |")
            cTurn = False
        elif cScore > 16:
            # Stand when score is greater than 16
            cTurn = False
        else:
            cScore = hitMe(cScore)
    if cTurn == False and pTurn == False:
        # both turns have commenced, check score and produce a winner
        winner = checkWinner(pScore,cScore)
        if winner == "player":
            pWins = pWins + 1
        elif winner == "computer":
            pLoss = pLoss + 1
        print(f"| Player Wins: {pWins} | Player Losses: {pLoss} |")
        # ask if player wants to play again
        pAgain = playAgain()
        if pAgain == "Yes":
            # Increment round by 1, pass win and loss count back to the game start
            gameRound((gRound + 1),pWins,pLoss)
        elif pAgain is None:
            print(f"| Final Score: {gRound} rounds played | ")
            print(f"| Player Wins: {pWins} | Player Losses: {pLoss} |")
            print("Thank y'inz for playing, n'at.")
    
def playAgain():
    # Input request to start the game over
    print("| Would you like to play again? [Yes or enter to quit] |")
    bInput = input("| Yes | ")
    # Return valid input to the calling function
    if bInput == "Yes":
        return bInput
    else:
        return None
        # Anything other than an explicit "Yes" will close the game without error

def main():
    # Welcome the player
    print("|=-Welcome to Vanessa's Game of 21-=|")
    # start the game with gRound = 1, pWins = 0, pLoss = 0
    gameRound(1,0,0)

main()