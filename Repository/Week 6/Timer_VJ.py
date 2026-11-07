# We need the sleep function contained within the time module, so we import it
import time

# Check if input is an integer - Returns None if the input cannot be turned into an integer and returns the number if it is valid
def is_integer(value):
    try:
        return int(value)
    except ValueError:
        return None

# Input loop to verify entries are valid
# We know we're working with an integer when is_integer returns a number so we can safely use it to determine if a number is negative or not. 
# This validates the entry is not a string, and not negative
def getInput():
    while True:
        print('Enter desired seconds (positive integer) to begin the countdown')
        tinput = is_integer(input("🐋 ->"))
        if tinput is not None and tinput > 0:
            return tinput
        elif tinput == 0:
            print('🚫 The integer must be greater than 0! 🚫')
        else:
            print('🚫 You must enter a non-negative integer! 🚫')

# Define a function to display the countdown
# We put the repeat function here so that it will continue to prompt repeating until the user chooses to exit the program
# The sleep function we're running from the time module pauses the execution of the script for the specified number of seconds 
def countdown_timer(seconds):
    for second in reversed(range(1, seconds + 1)):
        print(f"⌛ Time remaining: {second} second(s) ⌛")
        time.sleep(1)
    print("⏰ Times up! ⏰")
    repeat(seconds)

# Define a function to be called after the timer runs, prompting user to repeat or exit
# We pipe the seconds variable through this function back into the countdown timer so we don't have to prompt input again
def repeat(seconds):
    print('Enter \"r\" to repeat the timer or press enter to exit')
    n = input("🐋 ->")
    if n == "r":
        countdown_timer(seconds)

# Get input and then perform the countdown
def main():
    seconds = getInput()
    countdown_timer(seconds)

# Run the program
main()