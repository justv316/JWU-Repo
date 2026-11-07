def isNotFloat(value):
    # Loops the input if the value is capable of being turned into a float
    try:
        float(value)
    except ValueError:
        return value

def isFloat(value):
    # Loops the input if the value is not a float
    try:
        return float(value)
    except ValueError:
        return None

def getaInput():
    # Get String input
    while True:
        ainput = isNotFloat(input('|-=--------------------What car do you want?-------------------=-|'))
        if ainput is not None:
            return ainput
        else:
            print("|-=------------------You must enter a string-------------------=-|")

def getbInput():
    # Get Float input
    while True:
        binput = isFloat(input('|-=----------------How much is it worth to you-----------------=-|'))
        if binput is not None:
            return binput
        else:
            print("|-=------------------You must enter a number-------------------=-|")
                   

def carFeeCalc(value):
    # Set constants based on specs
    ADM = 1000.00
    PRO_FEE = 100.00
    DES_FEE = 495.00
    UND_FEE = 295.00
    RUS_FEE = 395.00
    PRE_FEE = 250.00
    SLE_MULT = 0.05
    RES_MULT = 0.12
    # Calculate Fees
    constantFees = ADM + PRO_FEE + DES_FEE + UND_FEE + RUS_FEE + PRE_FEE
    sleFee = value * SLE_MULT
    resFee = value * RES_MULT
    # Return the total fees to main
    return constantFees + sleFee + resFee

def main():
    print("|-=Welcome to Average Used Car Dealership! An Amazon subsidiary=-|")
    print("|-=--------------------Tell us your desires--------------------=-|")
    carString = getaInput()
    carFloat = getbInput()
    carCost = carFeeCalc(carFloat) + carFloat
    print(f"|-=----------------{carString} will cost {carCost}=-|")
    print("|-=---------------------------Sucker---------------------------=-|")

main()