def is_integer(value):
    try:
        return int(value)
    except ValueError:
        return None

def inputlist():
    num = 2
    state = 0
    inputs = []
    while state < num:
        tinput = is_integer(input('Enter a number: '))
        if tinput is not None:
            inputs.append(tinput)
            state += 1
        else:
            print('You must enter a valid number')
    return inputs

    
def subtraction(inputs):
    difference = inputs[0] - inputs[1]
    return difference

def main():
    inputs = inputlist()
    difference = subtraction(inputs)
    print("difference = ",difference)

main()