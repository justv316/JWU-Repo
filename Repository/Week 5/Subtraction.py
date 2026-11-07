# highly commentated as this is a "Your-First-Python" program assignment, so I am clearly detailing my thought process in the construction of the program
# i may have gone a bit too far
# functions

# define a function that attempts to convert our input to an integer, and handles the error without terminating the program
    # returns boolean as its used as a conditional
def is_number(value):
    # Inputs can be 1 or negative so we use a different check on the inputs than the input count check. 
    try:
        int(value) # We only care if this input can be successfully turned into an integer
        return True # Valid input
    except ValueError:
        return False # Invalid input

# define a function that gathers the required number of inputs
    # our problem requires 2 inputs but this can support any positive integer
    # i wanted to work with program states and while loops 
def inputnum(num):
    inputs = [] # a list to store valid inputs
    state = int(0) # keep track of how many inputs we've added so that if there's an error it doesn't interrupt the input process.
    while state < num:
        tinput = input('Enter a number: ')
        if is_number(tinput):
            tinput = int(tinput) # convert it to an integer since we now know its not going to cause an error, this adds a computational step, but checking if something is actually a number is seemingly more complicated in python than it ought to be
            inputs.append(tinput) # add input to the list of inputs
            state += 1 # increment state by 1 only when we receive a valid input. 
        else: # catch non-int's
            print('You must enter a valid number') # prints error but doesn't terminate program
    subtraction(inputs) # now that we've completed our input loop, we perform the operation
# define a function that performs the intended operation on our list
    # a - b - c ... n is the same thing as a - (b + c + ... n)
    # subtract the sum of the 2nd to the last item in the list from the first item in the list
def subtraction(inputs):
    product = inputs[0] - sum(inputs[1:]) # python notation states [n:] will reference every item from that index onwards to its end, much simpler than the same process in powershell 
    print("product = ",product) # the end of our program

# we could now create functions that support other mathematical operations on the same input loop, which could be used to create a calculator.
    # we would then ask what operation is needed to be performed
# this could be a method of performing operations on groups of numbers, rather than simply 2 inputs
    # a simpler program could be written that does not check how many inputs are required, but establishing a flexible limit on the number of inputs we're receiving allows the use of a loop that checks the validity of inputs without terminating the program
# we could ask if the input is greater than 2, and perform a different, less resource intensive operation if not. 

#initialization
def init():
    try:
        num = int(input('How many inputs are there? [Min: 2] '))
    except:
        print('You must enter a whole number') # catch non-number inputs
        init() # start over
    else:
        if(num < 0):
            print('Input count must be positive') # catch negative numbers
            init() # start over
        elif(num == 1):
            print('You must specify at least 2 inputs') # catch the number 1
            init() # start over
        else:
            # Our input count is a valid number, so we proceed to accepting inputs.
            inputnum(num)  

#run the program
init()