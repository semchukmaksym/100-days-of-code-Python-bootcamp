def greet():
    print("Hello Maksym")

greet()

# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Maksym")


def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left\n")


life_in_weeks(20)

# Functions with more that 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional arguments

greet_with("Maksym", "London")

# Keyword arguments

greet_with(name="London", location="Maksym")