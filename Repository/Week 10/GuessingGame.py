import random as r

def isValid(value):
    # A list containing valid input strings
    validInput = ["High","Low","Correct"]
    # Return the string if it's one of the 3 terms
    if value in validInput:
        return value
    else:
        return None

def userVerification():
    # Get input
    aInput = isValid(input("[High, Low, Correct] > "))
    # Return input to the guessLoop
    if aInput is not None:
        return aInput
    else:
        print("You must make a valid selection")

def compGuess(lower,upper):
    # Produce a random number between specified ranges
    return r.randrange(lower,upper)

def guessLoop():
    # The computer only gets 5 guesses
    counter = 5
    # Default lower limit
    INIT_LOWER = 1
    # Default upper limit
    INIT_UPPER = 100
    # Store the current guess as a variable to replace one of the ceilings.
    currentGuess = compGuess(INIT_LOWER,INIT_UPPER)
    while counter > 0:
        print(f"Is the number {currentGuess}?")
        # Provide verification
        a = userVerification()
        if a == "High":
            counter -= 1
            # Set the upper limit to the current guess and create a new guess
            currentGuess = compGuess(INIT_LOWER,currentGuess)
        if a == "Low":
            counter -= 1
            # Set the lower limit to the current guess and create a new guess
            currentGuess = compGuess(currentGuess,INIT_UPPER)
        if a == "Correct":
            print("Yay! :)")
            # stop the loop
            break
    else:
        # Counter reached 0 after 5 attempts so sad
        print("Aw :(")

def main():
    # Start the game
    guessLoop()

main()