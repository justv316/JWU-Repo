# Assignment objectives
# [Objective 1] For each round, the player starts with 0 | [Comment Line 109]
# [Objective 2] You should keep track of the wins and losses for the player | [Comment line 106]
# [Objective 3] You should repeatedly ask the player if they would like another card until they answers no | [Comment Line 40]
# [Objective 4] Each time the player asks for another card, generate a random number between 2 and 11. Display the player’s updated score. | [Comment Line 22 & 43]
# [Objective 5] If the player’s card puts them over 21, they busts. Print out that they busted and count this as a loss | [Comment Line 55 & 97]
# [Objective 6] Once the player has stopped, the dealer (the computer) gets to go | [Comment Line 121]
# [Objective 7] The computer starts at 0 and takes cards using the following rule: if the total is less than 16, it takes another card. If it is 16 or higher, it stays. | [Comment Line 26 & 111]
# [Objective 8] If the computer gets over 21, it busts and the player wins| [Comment line 31]
# [Objective 9] If the player has a higher score than the computer, the player wins, and one is added to the player’s wins | [Comment line 91]
# [Objective 10] If the player has a lower score, the player loses, and one is added to the player’s losses |  [Comment Line 95]
# [Objective 11] If both the player and the computer have the same score, the game is a tie and no win or loss is recorded |  [Comment Line 102]
# [Objective 12] You should print out the score for both the player and computer and who won the round [Comment Line 89]
# [Objective 13] After each round, you should ask if the player wants to play again. If so, play another round. If not, output the final number of wins and losses and end the program. | [Comment Line 130]


# we need random to generate a random number, assign it as r for ease of use
import random as r

def hitMe(value):
    # Helper function, adds a number between 2 and 11 to input
    # [Objective 4] generate a random number between 2 and 11
    return value + r.randrange(2,12)

def cTurn(cScore):
    # [Objective 7] Computer will 'stand' 16 or higher so we hit while score is less than 16
    while cScore < 16:
        cScore = hitMe(cScore)
        print(f"| Computer score is {cScore} |")
    if cScore > 21:
        # [Objective 8] Greater than 21 is a bust
        print("| The computer busted! |")
        return cScore
    else:
        # 'stand'
        return cScore

def pTurn (pScore):
    print(f"| Current hand value is {pScore} |")
    # [Objective 3] Ask player to hit until they stand or bust
    while playerInput() != "stand" and pScore <= 21:
        pScore = hitMe(pScore)
        # [Objective 4] Display the updated score
        print(f"| Current hand value is {pScore} |")
        if pScore > 21:
            print("| You have busted! |")
            break
        elif pScore == 21:
            print("| You scored 21! |")
            break
    return pScore

def playerInput():
    # Helper function for capturing input
    while True:
        aInput = isaValid(input("| [Hit,Stand,hit,stand] |"))
        # Return valid input to the calling function
        if aInput == "Hit" or aInput == "hit":
            return aInput
        elif aInput == "Stand" or aInput =="stand":
            # pTurn is expecting "stand" but accepts "Stand" as well
            return "stand"
        # Ask again if an invalid entry
        else:
            print("You must make a valid selection [Hit,Stand,hit,stand]")

def isaValid(value):
    # Helper function for input validation
    validInput = ["Hit","Stand","hit","stand"]
    # Return valid input to the calling function
    if value in validInput:
        return value
    else:
        return None

def playAgain():
    # Helper function to request to start the game over
    print("| Would you like to play again? [Yes or enter to quit] |")
    bInput = input("| Yes | ")
    if bInput == "Yes":
        # Return valid input to the calling function
        return bInput
    else:
        # Anything other than an explicit "Yes" will close the game without error
        return None

def checkWinner(pScore,cScore):
    # [Objective 12] Print the score for both player and computer then display winner
    print(f"Player Hand: {pScore} Computer Hand: {cScore}")
    if (pScore > cScore and pScore <= 21) or cScore > 21 :
        # [Objective 9] The player wins when their score is greater than the computers and less than or equal to 21
        print("Player Win! Computer Loss!")
        return "player"
    elif pScore < cScore or pScore > 21:
        # [Objective 10 & Objective 5] The player loses when the computer score is greater than the players or when player score is greater than 21(bust)
        print("Computer Win! Player Loss!")
        return "computer"
    elif pScore == cScore:
        # [Objective 11] When both player and computer have the same score the game is tied and no win or loss is recorded
        print("It's a draw!")
        return None
    
def gameRound(gRound,pWins,pLoss):
    # Start round
    print(f"| It is round {gRound} |")
    # [Objective 2] Keep track of wins and losses
    print(f"| Wins: {pWins} |")
    print(f"| Losses: {pLoss} |")
    # [Objective 1] pScore starts at 0
        # Then, we 'give the player a card' and begin their turn by calling pTurn with hitMe(0)
    # [Objective 7] Computer score starts at 0
        # When the player 'busts' the computer turn is skipped, so we must initalize the variable as 0 here.
    cScore = 0
    pScore = pTurn(hitMe(0))
    # [Objective 5]
        # Greater than 21 is an auto-loss for the player and the cTurn is skipped
        # A 21 is not an auto-win per the assignment so we must give the computer a turn on 21
    if pScore <= 21:
        # [Objective 6] After the player goes, the computer gets a turn
        cScore = cTurn(hitMe(0))
    winner = checkWinner(pScore,cScore)
    if winner == "player":
        pWins = pWins + 1
    elif winner == "computer":
        pLoss = pLoss + 1
    print(f"| Player Wins: {pWins} | Player Losses: {pLoss} |")
    # [Objective 13] ask if player wants to play again
    pAgain = playAgain()
    if pAgain == "Yes":
        # Increment round by 1, pass win and loss count back to the game start
        gameRound((gRound + 1),pWins,pLoss)
    elif pAgain is None:
        print(f"| Final Score: {gRound} rounds played | ")
        print(f"| Player Wins: {pWins} | Player Losses: {pLoss} |")
        print("Thank y'inz for playing, n'at.")

def main():
    # Welcome the player
    print("|=-Welcome to Vanessa's Game of 21-=|")
    # start the game with gRound = 1, pWins = 0, pLoss = 0
    gameRound(1,0,0)

main()