# Faulty Odd or Even Checker

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

main()