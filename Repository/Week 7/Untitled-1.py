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

def subtraction(*args):
    return args[0] - sum(args[1:])

def main():
    print(f"Difference is: {subtraction(1,5,6)}")

main()