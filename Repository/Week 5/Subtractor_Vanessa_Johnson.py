def is_integer(value):
    try:
        return int(value)
    except ValueError:
        return None

def getInput():
    while True:
        tinput = is_integer(input('Enter a number: '))
        if tinput is not None:
            return tinput
        else:
            print('You must enter a valid number')
    
def subtraction(d1,d2):
    return d1 - d2

def main():
    d1 = getInput()
    d2 = getInput()
    d3 = subtraction(d1,d2)
    print(d1," - ",d2," = ",d3)

main()