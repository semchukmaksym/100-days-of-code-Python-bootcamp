try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}")


