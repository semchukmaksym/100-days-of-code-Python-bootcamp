import art

print(art.logo)

def add(a,b):
    return a + b


def subtract(a,b):
    return a - b


def multiply(a,b):
    return a * b


def divide(a,b):
    return a / b


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator(a,b,c):
    return operations[c](a,b)

# Program asks the user to type the first number
# Program asks the user to type mathematical operator
# Program asks the user to type the second number
# Program works out the result based on the chosen math operator
# Program asks if the user wants to continue working with the previous result
# If yes - program loops to use the previous result as the first number and then repeats the calculation
# If no program asks the user the first number again and wipes all memory of previous

condition = True

def main_calculator ():
    first_number = float(input("Please enter the first number:\n"))

    while condition:
        for symbol in operations:
            print(symbol)

        math_operation = input("Please enter the math operator:\n")
        second_number = float(input("Please enter the second number:\n"))
        result = calculator(first_number, second_number, math_operation)

        print(f"{first_number} {math_operation} {second_number} = {result}")

        choice = input("Press 'y' if you want to continue or 'n' if you want to start new calculation?")

        if choice == "y":
            first_number = result
        elif choice == "n":
            print("\n" * 20)
            main_calculator()


main_calculator()