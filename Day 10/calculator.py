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

condition = True

total_score = 0

def calculator(a,b,c):
    return operations[c](a,b)

first_number = int(input("Please enter the first number:\n"))
math_operation = input("Please enter the math operator:\n")
second_number = int(input("Please enter the second number:\n"))






