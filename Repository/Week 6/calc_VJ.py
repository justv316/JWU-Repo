# Check if input is an integer - Returns None if the input cannot be turned into an integer and returns the number if it is valid
def is_integer(value):
    try:
        return int(value)
    except ValueError:
        return None

# Input loop to verify entries are valid numbers
# Safely catches invalid inputs like strings and floats without terminating the program
def getInput():
    while True:
        tinput = is_integer(input('Enter a number: '))
        if tinput is not None:
            return tinput
        else:
            print('You must enter a valid number')

# Mathematical functions that performs stated operation on inputs

def addition(d1,d2):
    return d1 + d2

def subtraction(d1,d2):
    return d1 - d2

def multiplication(d1,d2):
    return d1 * d2

def division(d1,d2):
    return d1 / d2

# Get inputs and then perform calculations, printing the formatted results
def main():
    d1 = getInput()
    d2 = getInput()
    sum = addition(d1,d2)
    diff = subtraction(d1,d2)
    prod = multiplication(d1,d2)
    quot = division(d1,d2)
    print(d1,"+",d2,"=",sum)
    print(d1,"-",d2,"=",diff)
    print(d1,"x",d2,"=",prod)
    print(d1,"/",d2,"=",quot)

# Run the program
main()