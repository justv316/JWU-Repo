import time

# Check if input is an integer - Returns None if the input cannot be turned into an integer and returns the number if it is valid

def is_integer(value):
    return int(value)

# Input loop to verify entries are valid
# We know we're working with an integer so we can safely use it to determine if a number is negative or not. 
# We could also utilize a regex match of the "-" character, since "5-5" and "-5" are both invalid inputs but for different reasons. 

def getInput():
    while True:
        print('Enter desired seconds (positive integer) to begin the countdown')
        return is_integer(input(">>"))
        #if tinput is not None and tinput >= 0:
        #    return tinput
        #else:
        #    print('You must enter a valid, non-negative, integer!')

# Define a function to display the countdown
# We put the repeat function here so that it will continue to prompt repeating after the first repeat
def countdown_timer(seconds):
    for second in reversed(range(1, seconds + 1)):
        print(f"Time: {second} second(s)")
        time.sleep(1)
    print("⏰Times up!")
    repeat(seconds)

# Define a function to be called after the timer runs, prompting user to repeat, or exit
def repeat(seconds):
    print('Enter r to repeat the timer or press enter to exit')
    n = input(">>")
    if n == "r":
        countdown_timer(seconds)

# Get input and then perform the countdown
def main():
    seconds = getInput()
    countdown_timer(seconds)

# Run the program
main()