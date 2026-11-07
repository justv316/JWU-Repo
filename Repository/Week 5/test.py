def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def inputnum(num):
    inputs = []
    state = int(0)
    while state < num:
        tinput = input('Enter a number: ')
        if is_number(tinput):
            tinput = int(tinput)
            inputs.append(tinput)
            state += 1
        else:
            print('You must enter a valid number')
    subtraction(inputs)

def subtraction(inputs):
    product = inputs[0] - sum(inputs[1:])
    print("product = ",product)

def init():
    try:
        num = int(input('How many inputs are there? [Min: 2] '))
    except:
        print('You must enter a whole number')
        init()
    else:
        if(num < 0):
            print('Input count must be positive')
            init()
        elif(num == 1):
            print('You must specify at least 2 inputs')
            init()
        else:
            inputnum(num)  

init()